# 💻 COBOL-Tutor

**Interaktiver KI-gestützter COBOL-Kurs mit Google Gemini AI**

Lerne COBOL von Grund auf bis zum vollständigen Lotto-Generator mit praktischen Übungen, Live-Code-Ausführung und KI-Unterstützung!

## 🎯 Features

- **15 strukturierte Lektionen** - Von Basics bis zum kompletten Lotto-Programm
- **Live Code-Editor** - Schreibe und teste COBOL direkt im Browser
- **KI-Tutor** - Stelle Fragen und erhalte sofortige Hilfe (Google Gemini)
- **Code-Analyse** - Lass deinen Code analysieren und Feedback erhalten
- **Übungen mit Lösungen** - Praktische Aufgaben zu jeder Lektion
- **Interaktive Hinweise** - KI-generierte Tipps ohne die Lösung zu verraten
- **Vollständig kostenlos** - Nutzt Google's kostenlosen Gemini API

## 📚 Lektionen-Übersicht

### Grundlagen (Lektionen 1-5)
1. **COBOL Basics** - Struktur und DISPLAY
2. **Variablen** - Datentypen und WORKING-STORAGE
3. **Arithmetik** - Berechnungen mit COMPUTE
4. **IF-Bedingungen** - Entscheidungen treffen
5. **Schleifen** - PERFORM VARYING

### Fortgeschritten (Lektionen 6-11)
6. **Benutzereingabe** - ACCEPT-Anweisung
7. **Arrays** - OCCURS und Tabellen
8. **Zufallszahlen** - FUNCTION RANDOM
9. **Duplikate** - Erkennung doppelter Werte
10. **Sortierung** - Bubble-Sort Algorithmus
11. **Paragraphen** - Strukturierte Programmierung

### Lotto-Projekt (Lektionen 12-15)
12. **Einfacher Lotto-Generator** - Grundgerüst
13. **Lotto ohne Duplikate** - Einzigartige Zahlen
14. **Lotto mit Sortierung** - Sortierte Ausgabe
15. **Vollständiger Generator** - Professionelles Programm 🎓

## 🚀 Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)
- Git (optional, für Clone)

### Schritt 1: Repository herunterladen

```bash
# Mit Git
git clone <repository-url>
cd cobol-tutor

# Oder ZIP herunterladen und entpacken
```

### Schritt 2: Python-Pakete installieren

```bash
pip install -r requirements.txt
```

### Schritt 3: Google Gemini API-Key erstellen

1. Besuche [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Melde dich mit deinem Google-Konto an
3. Klicke auf "Create API Key"
4. Kopiere den generierten Key (beginnt mit "AIza...")

**Wichtig:** Der API-Key ist **100% kostenlos**!

### Schritt 4: API-Key konfigurieren

#### Option A: In der Anwendung eingeben
- Starte die Anwendung
- Gib den API-Key in der Sidebar ein

#### Option B: .env Datei erstellen
```bash
# Erstelle .env Datei im Projektverzeichnis
echo "GEMINI_API_KEY=dein-api-key-hier" > .env
```

### Schritt 5: Anwendung starten

```bash
streamlit run app.py
```

Die Anwendung öffnet sich automatisch im Browser unter `http://localhost:8501`

## 🖥️ Verwendung

### Code-Editor

1. Wähle eine Lektion in der Sidebar
2. Wechsle zum Tab "💻 Code-Editor"
3. Schreibe deinen COBOL-Code
4. Klicke auf "▶️ Code ausführen"

**Hinweis:** Beim ersten Start wird GnuCOBOL automatisch installiert (kann 1-2 Minuten dauern)

### Übungen

1. Wechsle zum Tab "🎯 Übung"
2. Lies die Aufgabe
3. Schreibe deine Lösung
4. Klicke auf "✅ Lösung prüfen"
5. Erhalte Feedback vom KI-Tutor

### KI-Tutor

1. Wechsle zum Tab "💬 KI-Tutor"
2. Stelle Fragen zu COBOL
3. Erhalte sofortige, ausführliche Antworten
4. Der Tutor kennt den Kontext der aktuellen Lektion

### Code-Analyse

- Klicke auf "🔍 Code analysieren" im Editor
- Erhalte Feedback zu:
  - Struktur und Syntax
  - Best Practices
  - Verbesserungsmöglichkeiten

## 📋 Beispiel-Session

```cobol
      IDENTIFICATION DIVISION.
      PROGRAM-ID. HELLOWORLD.
      
      PROCEDURE DIVISION.
          DISPLAY "Hello, COBOL World!".
          STOP RUN.
```

**Ausgabe:**
```
Hello, COBOL World!
```

## 🎓 Lernpfad

**Empfohlener Weg zum Lotto-Generator:**

1. **Woche 1:** Lektionen 1-5 (Grundlagen)
2. **Woche 2:** Lektionen 6-8 (Eingabe, Arrays, Zufall)
3. **Woche 3:** Lektionen 9-11 (Duplikate, Sortierung, Struktur)
4. **Woche 4:** Lektionen 12-15 (Lotto-Projekt)

**Tipp:** Nimm dir Zeit für die Übungen - Praxis ist entscheidend!

## 🛠️ Technische Details

### Komponenten

- **app.py** - Hauptanwendung (Streamlit)
- **lessons.py** - Alle 15 Lektionen mit Beispielen und Übungen
- **ai_tutor.py** - KI-Tutor Logik (Google Gemini Integration)
- **cobol_executor.py** - COBOL Code Compiler und Executor
- **models_list.py** - Hilfsprogramm für verfügbare AI-Modelle

### COBOL-Ausführung

Die Anwendung nutzt **GnuCOBOL** (Open Source COBOL Compiler):
- Wird automatisch bei erster Nutzung installiert
- Kompiliert COBOL zu nativen Binaries
- Führt Programme in isolierter Umgebung aus
- Unterstützt COBOL-85 und COBOL-2002 Standards

### KI-Integration

- **Model:** Google Gemini 2.5 Flash (schnell & kostenlos)
- **Capabilities:**
  - Code-Analyse
  - Fehler-Erklärung
  - Konzept-Erklärung
  - Interaktive Hilfe
  - Kontext-bewusste Antworten

## 🔧 Konfiguration

### Umgebungsvariablen

```bash
# .env Datei
GEMINI_API_KEY=your-api-key-here
GEMINI_MODEL=models/gemini-2.5-flash  # Optional
```

### Streamlit Konfiguration

Erstelle `.streamlit/config.toml` für Anpassungen:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"

[server]
port = 8501
headless = false
```

## 🐛 Fehlerbehebung

### GnuCOBOL Installation schlägt fehl

```bash
# Manuell installieren (Linux/Ubuntu)
sudo apt-get update
sudo apt-get install gnucobol4

# macOS mit Homebrew
brew install gnu-cobol

# Windows: Siehe OpenCobolIDE
```

### API-Key funktioniert nicht

- Überprüfe, ob der Key mit "AIza" beginnt
- Erstelle einen neuen Key in [AI Studio](https://aistudio.google.com/app/apikey)
- Prüfe die .env Datei auf Tippfehler

### Kompilierungsfehler

- Achte auf korrekte Spalten-Ausrichtung:
  - Spalte 7: Kommentare (*)
  - Spalte 8-11: Area A (DIVISION, SECTION, Paragraphen)
  - Spalte 12-72: Area B (Anweisungen)

### Code läuft nicht

- Prüfe, ob alle Anweisungen mit einem Punkt (.) enden
- Verwende END-IF, END-PERFORM für Block-Strukturen
- Achte auf STOP RUN am Ende

## 📖 Ressourcen

### COBOL lernen

- [COBOL Tutorial](https://www.tutorialspoint.com/cobol/)
- [GnuCOBOL Manual](https://gnucobol.sourceforge.io/)
- [COBOL Programming Guide](https://www.ibm.com/docs/en/cobol-zos)

### Google Gemini

- [Gemini API Docs](https://ai.google.dev/docs)
- [AI Studio](https://aistudio.google.com/)

## 🤝 Beitragen

Verbesserungsvorschläge sind willkommen!

1. Fork das Repository
2. Erstelle einen Feature Branch
3. Committe deine Änderungen
4. Push zum Branch
5. Erstelle einen Pull Request

## 📝 Lizenz

Dieses Projekt ist Open Source und für Bildungszwecke frei verfügbar.

## 💡 Tipps für Anfänger

1. **Start langsam** - Beginne mit Lektion 1, überspringe keine
2. **Übe viel** - Versuche jede Übung selbst zu lösen
3. **Frage den Tutor** - Keine Frage ist zu dumm
4. **Experimentiere** - Ändere Code und schau was passiert
5. **Fehler sind OK** - Sie gehören zum Lernen dazu

## 🎉 Erfolge feiern

Nach Abschluss aller 15 Lektionen kannst du:

- ✅ COBOL-Programme von Grund auf schreiben
- ✅ Mit Variablen, Arrays und Schleifen arbeiten
- ✅ Benutzereingaben verarbeiten
- ✅ Zufallszahlen generieren
- ✅ Sortieralgorithmen implementieren
- ✅ Strukturierte Programme mit Paragraphen erstellen
- ✅ Einen vollständigen Lotto-Generator bauen

**Herzlichen Glückwunsch! 🎓**

## 📞 Support

Bei Fragen oder Problemen:

1. Nutze den KI-Tutor in der Anwendung
2. Prüfe die Fehlerbehebung oben
3. Erstelle ein Issue im Repository

---

**Viel Erfolg beim Lernen von COBOL! 🚀**

*Made with ❤️ and AI*
