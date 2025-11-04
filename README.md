# 💻 COBOL-Tutor 🆓

Ein **100% kostenloser** interaktiver COBOL-Kurs mit KI-Unterstützung!

Powered by **Google Gemini** - Komplett kostenlos nutzbar! ✨

---

## 🚀 Schnellstart (Lokal)

### 1️⃣ Repository klonen
```bash
git clone <dein-repo>
cd cobol-tutor
```

### 2️⃣ Dependencies installieren
```bash
pip install -r requirements.txt
```

### 3️⃣ Gemini API-Key holen (KOSTENLOS!)
1. Gehe zu: https://aistudio.google.com/app/apikey
2. Klicke "Create API Key"
3. Kopiere den Key

### 4️⃣ API-Key setzen
**Option A:** In der App-Sidebar eingeben  
**Option B:** `.env` Datei erstellen:
```bash
cp .env.example .env
# Trage deinen Key ein
```

### 5️⃣ App starten
```bash
streamlit run app.py
```

---

## ☁️ Deployment auf Streamlit Cloud (KOSTENLOS!)

### Schritt 1: GitHub Repository erstellen
1. Gehe zu https://github.com/new
2. Erstelle ein neues Repository (z.B. "cobol-tutor")
3. Repository kann public oder private sein

### Schritt 2: Code hochladen
```bash
# In deinem cobol-tutor Ordner:
git init
git add .
git commit -m "Initial commit - COBOL Tutor"
git remote add origin https://github.com/DEIN-USERNAME/cobol-tutor.git
git push -u origin main
```

### Schritt 3: Bei Streamlit Cloud deployen
1. Gehe zu: https://share.streamlit.io/
2. Klicke "New app"
3. Wähle dein GitHub Repository
4. Main file: `app.py`
5. **WICHTIG:** Füge unter "Advanced settings" → "Secrets" hinzu:
   ```toml
   GEMINI_API_KEY = "dein_api_key_hier"
   ```
6. Klicke "Deploy"

### 🎉 Fertig!
Deine App ist jetzt online unter:
`https://DEIN-USERNAME-cobol-tutor.streamlit.app`

---

## 🌟 Features

✅ **5 interaktive Lektionen**: Von Basics bis Schleifen  
✅ **KI-Tutor**: Beantwortet alle Fragen (auf Deutsch!)  
✅ **Live Code-Ausführung**: Teste COBOL direkt im Browser  
✅ **Übungen mit Feedback**: Automatische Bewertung  
✅ **100% Kostenlos**: Dank Google Gemini API  

---

## 📚 Lektionen

1. **COBOL Basics** - Struktur und DISPLAY
2. **Variablen** - Datentypen und PIC
3. **Arithmetik** - Berechnungen
4. **IF-Bedingungen** - Verzweigungen
5. **Schleifen** - PERFORM

---

## 💡 Nutzung

1. **Lektion wählen** in der Sidebar
2. **Theorie lesen** im ersten Tab
3. **Code ausprobieren** im Editor
4. **Übungen lösen** mit KI-Feedback
5. **Fragen stellen** an den Tutor

---

## 🆓 Kostenlose Limits

**Google Gemini Free Tier:**
- ✅ 60 Anfragen/Minute
- ✅ 1.500 Anfragen/Tag
- ✅ Komplett kostenlos!

Das reicht für **normale Nutzung mehr als aus**! 🎉

---

## 🔧 Technische Details

**Stack:**
- Python 3.8+
- Streamlit (UI)
- Google Gemini API (KI)
- GnuCOBOL (Code-Ausführung, nur Linux)

**Hinweis:** COBOL-Ausführung funktioniert nur auf Linux-Servern (wie Streamlit Cloud). Auf Windows kannst du trotzdem lernen, Code analysieren und den Tutor nutzen!

---

## 📁 Projektstruktur

```
cobol-tutor/
├── app.py              # Hauptanwendung
├── ai_tutor.py         # KI-Tutor mit Gemini
├── cobol_executor.py   # COBOL Code-Ausführung
├── lessons.py          # Alle Lektionen
├── requirements.txt    # Dependencies
├── .env.example        # API-Key Template
├── .gitignore          # Git Ignore
└── README.md           # Diese Datei
```

---

## 🆘 Troubleshooting

**"API-Key fehlt"**  
→ Trage den Key in der Sidebar ein oder in `.env` Datei

**"Limit erreicht"**  
→ Warte kurz (Reset nach 1 Minute) oder erstelle neuen Key

**"COBOL Installation fehlgeschlagen"**  
→ Normal auf Windows! Funktioniert nur auf Linux (Streamlit Cloud ist Linux)

**"Module not found"**  
→ `pip install -r requirements.txt`

---

## 🎓 Über das Projekt

Dieses Projekt zeigt, wie man mit **kostenlosen KI-APIs** einen vollwertigen interaktiven Kurs erstellen kann!

**Perfekt für:**
- COBOL-Anfänger
- Legacy-Entwickler
- IT-Studenten
- Alle die COBOL lernen wollen

---

## 📝 Lizenz

MIT License - Nutze es wie du willst! 🎉

---

## 🤝 Beitragen

Verbesserungen? Pull Requests sind willkommen!

---

**Viel Erfolg beim COBOL-Lernen! 🚀**

*Powered by Google Gemini* 🤖
