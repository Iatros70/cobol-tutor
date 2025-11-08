"""
KI-Tutor Logik mit Google Gemini API (KOSTENLOS!)
"""
import google.generativeai as genai
import os

class CobolTutor:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            # Verwende das stabile gemini-pro Modell
            self.model = genai.GenerativeModel('gemini-1.5-flash')
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
    
    def get_response(self, user_message, conversation_history=None, current_lesson=None, code_result=None):
        if not self.model:
            return "⚠️ API-Key fehlt! Bitte setze GEMINI_API_KEY in der .env Datei oder gib ihn in der Sidebar ein."
        
        context = self.system_prompt + "\n\n"
        
        if current_lesson:
            context += f"\n\nAKTUELLE LEKTION: {current_lesson['title']}\n"
            context += f"Beschreibung: {current_lesson['description']}\n"
        
        if code_result:
            context += f"\n\nCODE-AUSFÜHRUNG:\n"
            context += f"Erfolg: {code_result['success']}\n"
            if code_result['output']:
                context += f"Ausgabe: {code_result['output']}\n"
            if code_result['error']:
                context += f"Fehler: {code_result['error']}\n"
        
        # Konversationshistorie aufbauen
        if conversation_history:
            context += "\n\nBisherige Konversation:\n"
            for msg in conversation_history[-5:]:  # Nur letzte 5 Nachrichten
                role = "User" if msg['role'] == 'user' else "Tutor"
                context += f"{role}: {msg['content']}\n"
        
        full_message = context + "\n\nUser: " + user_message
        
        try:
            response = self.model.generate_content(full_message)
            return response.text
            
        except Exception as e:
            error_msg = str(e)
            if "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
                return "❌ Ungültiger API-Key! Bitte prüfe deinen Gemini API-Key."
            elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
                return "⚠️ Kostenloses Limit erreicht. Warte kurz oder erstelle einen neuen Key bei https://makersuite.google.com/app/apikey"
            else:
                return f"❌ Fehler bei der API-Anfrage: {error_msg}"
    
    def analyze_code(self, code, expected_output=None):
        if not self.model:
            return "⚠️ API-Key fehlt!"
        
        prompt = self.system_prompt + f"""

Analysiere folgenden COBOL-Code:

```cobol
{code}
```

Gib Feedback zu:
1. Struktur und Syntax
2. Best Practices
3. Mögliche Verbesserungen
4. Ob der Code funktionieren sollte

Sei konstruktiv und ermutigend!"""

        if expected_output:
            prompt += f"\n\nErwartete Ausgabe: {expected_output}"
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"❌ Fehler: {str(e)}"
    
    def get_hint(self, exercise, user_code=None):
        if not self.model:
            return exercise.get('hint', 'Kein Hinweis verfügbar.')
        
        prompt = self.system_prompt + f"""

Der Schüler arbeitet an dieser Übung:

AUFGABE: {exercise['task']}

"""
        if user_code:
            prompt += f"Bisheriger Code:\n```cobol\n{user_code}\n```\n\n"
        
        prompt += "Gib einen hilfreichen Hinweis, der zum Nachdenken anregt, aber nicht die komplette Lösung verrät!"
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return exercise.get('hint', 'Kein Hinweis verfügbar.')