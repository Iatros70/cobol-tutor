"""
KI-Tutor Logik mit Google Gemini API (KOSTENLOS!)
"""
import os
import google.generativeai as genai


class CobolTutor:
    def __init__(self, api_key=None):
        # API-Key aus Parameter, Sidebar (ENV) oder .env
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')

        # Modell (Standard: schnelles & kostenloses Modell)
        self.model_name = os.getenv('GEMINI_MODEL', 'models/gemini-2.5-flash')

        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        else:
            self.model = None

        self.system_prompt = (
            "Du bist ein geduldiger und erfahrener COBOL-Lehrer. "
            "Erkläre, hilf und motiviere. Verwende deutsche Sprache, "
            "klare Beispiele und fördere das Verständnis.\n\n"
            "Erkläre die 4 Divisions, moderne Syntax und reale Anwendungen."
        )

    def _need_key(self):
        return "⚠️ API-Key fehlt! Bitte setze GEMINI_API_KEY in der .env Datei oder gib ihn in der Sidebar ein."

    def _handle_error(self, e: Exception):
        msg = str(e).lower()
        if "api key not valid" in msg or "api_key_invalid" in msg or "invalid api key" in msg:
            return "❌ Ungültiger API-Key! Bitte prüfe deinen Gemini AI Studio Key (beginnt mit 'AIza')."
        if "quota" in msg or "rate" in msg or "limit" in msg:
            return "⚠️ Kostenloses Limit erreicht. Warte kurz oder nutze einen neuen Key."
        if "not found" in msg or "is not supported" in msg or "404" in msg:
            return f"❌ Modell nicht verfügbar: `{self.model_name}`. Versuche z. B. `models/gemini-2.5-flash`."
        return f"❌ Fehler bei der API-Anfrage: {str(e)}"

    def get_response(self, user_message, conversation_history=None, current_lesson=None, code_result=None):
        if not self.model:
            return self._need_key()

        context = self.system_prompt + "\n\n"

        if current_lesson:
            context += f"AKTUELLE LEKTION: {current_lesson['title']}\n"
            context += f"Beschreibung: {current_lesson['description']}\n"

        if code_result:
            context += "\nCODE-AUSFÜHRUNG:\n"
            context += f"Erfolg: {code_result['success']}\n"
            if code_result.get('output'):
                context += f"Ausgabe: {code_result['output']}\n"
            if code_result.get('error'):
                context += f"Fehler: {code_result['error']}\n"

        if conversation_history:
            context += "\nBisherige Konversation:\n"
            for msg in conversation_history[-5:]:
                role = "User" if msg['role'] == 'user' else "Tutor"
                context += f"{role}: {msg['content']}\n"

        full_message = context + "\n\nUser: " + user_message

        try:
            response = self.model.generate_content(full_message)
            return response.text
        except Exception as e:
            return self._handle_error(e)

    def analyze_code(self, code, expected_output=None):
        if not self.model:
            return self._need_key()

        prompt = (
            self.system_prompt
            + f"\n\nAnalysiere folgenden COBOL-Code:\n```cobol\n{code}\n```\n"
            "Gib Feedback zu:\n"
            "1. Struktur und Syntax\n2. Best Practices\n3. Verbesserungen\n4. Läuft der Code korrekt?"
        )

        if expected_output:
            prompt += f"\n\nErwartete Ausgabe: {expected_output}"

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return self._handle_error(e)

    def get_hint(self, exercise, user_code=None):
        if not self.model:
            return exercise.get('hint', 'Kein Hinweis verfügbar.')

        prompt = self.system_prompt + f"\n\nAUFGABE: {exercise['task']}\n"
        if user_code:
            prompt += f"\nBisheriger Code:\n```cobol\n{user_code}\n```\n"

        prompt += "\nGib einen hilfreichen Hinweis, der zum Nachdenken anregt, aber nicht die komplette Lösung verrät."

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return exercise.get('hint', f"Kein Hinweis verfügbar. ({self._handle_error(e)})")
