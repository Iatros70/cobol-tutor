# 📦 COBOL-Tutor Installation

## Schnellstart (5 Minuten)

### 1. Python installieren

**Windows:**
- Lade Python 3.8+ von [python.org](https://www.python.org/downloads/)
- Wichtig: Hake "Add Python to PATH" an!

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### 2. Projekt herunterladen

```bash
# Mit Git
git clone <repository-url>
cd cobol-tutor

# ODER: ZIP herunterladen und entpacken
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

**Bei Problemen:**
```bash
# Verwende pip3 statt pip
pip3 install -r requirements.txt

# Oder mit virtualenv
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Google Gemini API-Key erstellen

1. Öffne [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Melde dich mit Google-Konto an
3. Klicke "Create API Key"
4. Kopiere den Key (beginnt mit "AIza...")

### 5. API-Key konfigurieren

**Option A: Direkt in der App** (empfohlen für Anfänger)
- Starte die App (Schritt 6)
- Gib den Key in der Sidebar ein

**Option B: .env Datei**
```bash
# Kopiere die Vorlage
cp .env.example .env

# Öffne .env und trage deinen Key ein
# GEMINI_API_KEY=dein-echter-key-hier
```

### 6. Anwendung starten

```bash
streamlit run app.py
```

**Automatisch öffnet sich:** `http://localhost:8501`

---

## Detaillierte Installation

### Windows

#### Python installieren

1. Lade Python von [python.org](https://www.python.org/downloads/)
2. Führe Installer aus
3. **WICHTIG:** ✅ "Add Python to PATH"
4. Klicke "Install Now"
5. Verifiziere Installation:

```cmd
python --version
pip --version
```

#### Projekt einrichten

```cmd
# Navigiere zum Download-Ordner
cd C:\Users\DeinName\Downloads\cobol-tutor

# Installiere Pakete
pip install -r requirements.txt

# Starte Anwendung
streamlit run app.py
```

### macOS

#### Mit Homebrew

```bash
# Homebrew installieren (falls nicht vorhanden)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python installieren
brew install python3

# Projekt einrichten
cd ~/Downloads/cobol-tutor
pip3 install -r requirements.txt
streamlit run app.py
```

### Linux (Ubuntu/Debian)

```bash
# System aktualisieren
sudo apt-get update

# Python und pip installieren
sudo apt-get install python3 python3-pip python3-venv

# Projekt einrichten
cd ~/Downloads/cobol-tutor
pip3 install -r requirements.txt

# Anwendung starten
streamlit run app.py
```

---

## Fehlerbehebung

### "python nicht gefunden"

**Windows:**
- Python neu installieren mit "Add to PATH"
- Oder verwende vollständigen Pfad: `C:\Python3X\python.exe`

**macOS/Linux:**
- Verwende `python3` statt `python`
- Füge Alias hinzu: `alias python=python3`

### "pip nicht gefunden"

```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### "streamlit nicht gefunden"

```bash
# Nochmals installieren
pip install streamlit --upgrade

# Oder direkt aufrufen
python -m streamlit run app.py
```

### "Port 8501 bereits belegt"

```bash
# Anderen Port verwenden
streamlit run app.py --server.port 8502
```

### API-Key Probleme

**Ungültiger Key:**
- Key muss mit "AIza" beginnen
- Keine Leerzeichen vor/nach dem Key
- Erstelle neuen Key in [AI Studio](https://aistudio.google.com/app/apikey)

**Quota erschöpft:**
- Warte ein paar Minuten
- Gemini hat großzügige kostenlose Limits
- Erstelle ggf. neuen Key

### GnuCOBOL Installation

**Automatische Installation schlägt fehl:**

```bash
# Linux/Ubuntu - Manuell installieren
sudo apt-get install gnucobol4

# macOS
brew install gnu-cobol

# Windows - OpenCobolIDE verwenden
# Download von: https://sourceforge.net/projects/open-cobol-ide/
```

---

## Virtuelle Umgebung (empfohlen)

### Warum virtuelle Umgebung?

- Isoliert Projekt-Abhängigkeiten
- Verhindert Konflikte mit anderen Python-Projekten
- Best Practice für Python-Entwicklung

### Setup

```bash
# Erstelle virtuelle Umgebung
python -m venv venv

# Aktiviere (Linux/macOS)
source venv/bin/activate

# Aktiviere (Windows)
venv\Scripts\activate

# Installiere Abhängigkeiten
pip install -r requirements.txt

# Starte Anwendung
streamlit run app.py

# Deaktiviere (wenn fertig)
deactivate
```

---

## Verifizierung

Nach erfolgreicher Installation solltest du:

1. ✅ Browser öffnet sich automatisch
2. ✅ COBOL-Tutor Interface ist sichtbar
3. ✅ 15 Lektionen in der Sidebar
4. ✅ Code-Editor funktioniert
5. ✅ KI-Tutor antwortet auf Fragen

**Test-Code:**
```cobol
      IDENTIFICATION DIVISION.
      PROGRAM-ID. TEST.
      
      PROCEDURE DIVISION.
          DISPLAY "Installation erfolgreich!".
          STOP RUN.
```

**Erwartete Ausgabe:**
```
Installation erfolgreich!
```

---

## Updates

### Anwendung aktualisieren

```bash
# Mit Git
git pull origin main
pip install -r requirements.txt --upgrade

# Ohne Git
# Lade neue Version herunter
# Entpacke und ersetze alte Dateien
pip install -r requirements.txt --upgrade
```

---

## Support

**Hilfe benötigt?**

1. Prüfe diese Anleitung nochmals
2. Suche in der README.md nach deinem Problem
3. Nutze den KI-Tutor in der Anwendung
4. Erstelle ein Issue im Repository

---

**Viel Erfolg! 🚀**
