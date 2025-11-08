"""
KI-Tutor Logik mit Google Gemini API (KOSTENLOS!)
"""
import os
import google.generativeai as genai

class CobolTutor:
    def __init__(self, api_key=None):
        # API-Key aus Parameter, Sidebar (ENV) oder .env
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')

        # Modell wählbar via ENV, sonst schneller & kostenloser Default
        self.model_name = os.getenv('GEMINI_MODEL', 'models/gemini-2.5-flash')

        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        else:
            self.model = None

        self.system_prompt = """Du bist ein geduldiger und erfahrener COBOL-Lehrer. Deine Aufgaben:

1. ERKLÄREN: Erkläre COBOL-Konzepte klar und mit Beispielen
2. HELFEN: Unterstütze bei Fehlern ohne direkt die Lösung zu verraten
3. MOTIVIEREN: Ermutige den Lernenden, auch bei Fehlern
4. ANPASSEN: Pass deine Erklärungen an das Niveau des Schülers an
5. FEEDBACK: Gib konstruktives Feedback zu Code

Wichtige Prinzipien:
- Verwende die Socratic Method: Stelle Fragen, die zum Verständnis führen
- Erkläre WARUM etwas funktioniert, nicht nur WIE
- Nutze Analogien und Beispiele aus dem echten Leben
- Bei Fehlern: Erkläre den Fehler, gib einen Hinweis, aber keine komplette Lösung (außer explizit gefragt)
- Sei freundlich und ermutigend
- Antworte auf Deutsch

COBOL-Spezifika:
- Erkläre die Struktur (4 Divisions)
- Weise auf COBOL-Eigenheiten hin
- Erkläre Business-Kontext (warum COBOL in Banken/Versicherungen)
- Verwende moderne COBOL-Syntax (free format)"""

    def _need_key(self):
        return "⚠️ API-Key fehlt! Bitte setze GEMINI_API_KEY in der .env Datei oder gib ihn in der Sidebar ein."

    def _handle_error(self, e: Exception):
        msg = str(e)
        low = msg.lower()
        if "api key not valid" in low or "api_key_invalid" in low or "invalid api key" in low:
            return "❌ Ungültiger API-Key! Bitte prüfe deinen Gemini AI Studio Key (beginnt mit 'AIza')."
        if "quota" in low or "rate" in low or "limit" in low:
            return "⚠️ Kostenloses Limit erreicht. Warte kurz oder nutze einen neuen Key."
        if "not found" in low or "is not supported for generatecontent" in low or "404" in low:
            return f"❌ Modell nicht verfügbar: `{self.model_name}`. Stelle GEMINI_MODEL auf ein vorhandenes Modell (z. B. `models/gemini-2.5-flash`)."
        return f"❌ Fehler bei der API-Anfrage: {msg}"

    def get_response(self, user_message, conversation_history=None, current_lesson=None, code_result=None):
        if not self.model:
            return self._need_key()

        context = self.system_prompt + "\n\n"

        if current_lesson:
            context += f"\n\nAKTUELLE LEKTION: {current_lesson['title']}\n"
            context += f"Beschreibung: {current_lesson['description']}\n"

        if code_result:
            context += f"\n\nCODE-AUSFÜHRUNG:\n"
            context += f"Erfolg: {code_result['success']}\n"
            if code_result.get('output'):
                context += f"Ausgabe: {code_result['output']}\n"
            if code_result.get('error'):
                context += f"Fehler: {code_result['error']}\n"

        if conversation_history:
            context += "\n\nBisherige Konversation:\n"
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

        prompt = self.system_prompt + f"""

Analysiere folgenden COBOL-Code:

```cobol
{code}
