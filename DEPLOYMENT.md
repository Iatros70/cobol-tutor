# 🚀 Deployment auf Streamlit Cloud

## In 10 Minuten online!

---

## 📋 Voraussetzungen

✅ GitHub Account (kostenlos)  
✅ Gemini API-Key (kostenlos von https://aistudio.google.com/app/apikey)

---

## Schritt 1: Gemini API-Key holen (2 Min)

1. Öffne https://aistudio.google.com/app/apikey
2. Klicke **"Create API Key"**
3. Wähle ein Projekt oder erstelle eins
4. **Kopiere den Key** (sieht aus wie: `AIzaSy...`)
5. **Speichere ihn sicher!**

---

## Schritt 2: GitHub Repository (3 Min)

### Option A: Neues Repo erstellen

```bash
# 1. Gehe zu https://github.com/new
# 2. Repository Name: cobol-tutor
# 3. Public oder Private (egal)
# 4. Erstellen!
```

### Option B: Code hochladen

```bash
# In deinem Projekt-Ordner:
git init
git add .
git commit -m "COBOL Tutor mit Gemini"
git remote add origin https://github.com/DEIN-USERNAME/cobol-tutor.git
git push -u origin main
```

---

## Schritt 3: Streamlit Cloud (5 Min)

### 1. Bei Streamlit anmelden
- Gehe zu: https://share.streamlit.io/
- Klicke **"Sign up"** mit GitHub
- Autorisiere Streamlit

### 2. App deployen
1. Klicke **"New app"**
2. Wähle dein Repository: `cobol-tutor`
3. Branch: `main`
4. Main file path: `app.py`

### 3. Secrets hinzufügen (WICHTIG!)
1. Klicke **"Advanced settings"**
2. Gehe zu **"Secrets"**
3. Füge ein:
   ```toml
   GEMINI_API_KEY = "AIzaSy....dein_key_hier"
   ```
4. Klicke **"Save"**

### 4. Deployen!
- Klicke **"Deploy"**
- Warte 2-3 Minuten
- **Fertig!** 🎉

---

## 🎊 Deine App ist online!

URL: `https://DEIN-USERNAME-cobol-tutor.streamlit.app`

---

## ⚙️ Konfiguration

### Secrets Format
```toml
# In Streamlit Cloud: Advanced Settings → Secrets
GEMINI_API_KEY = "dein_gemini_api_key"
```

### Optionale Einstellungen
```toml
# Weitere Konfiguration (optional)
[general]
email = "deine@email.com"
```

---

## 🔄 Updates deployen

Jedes Mal wenn du Code auf GitHub pushst, updated Streamlit automatisch:

```bash
git add .
git commit -m "Update XYZ"
git push
# Streamlit Cloud deployt automatisch!
```

---

## 📊 Monitoring

### Logs ansehen
1. Gehe zu https://share.streamlit.io/
2. Klicke auf deine App
3. **"Manage app"** → **"Logs"**

### Neustart
Bei Problemen: **"Reboot app"** in den Settings

---

## 💰 Kosten

### Streamlit Cloud
- ✅ **Kostenlos** für öffentliche Apps
- ✅ 1 GB RAM
- ✅ 1 CPU Core
- ✅ Unbegrenzter Traffic

### Gemini API
- ✅ **Kostenlos** bis 60 req/min
- ✅ 1.500 req/Tag
- ✅ Keine Kreditkarte nötig

**GESAMT: 0€ / Monat** 🎉

---

## 🎯 Teilen

Teile deine App:
```
https://DEIN-USERNAME-cobol-tutor.streamlit.app
```

Jeder kann sie kostenlos nutzen! 🌍

---

## 🐛 Troubleshooting

### "App startet nicht"
→ Prüfe Logs: Manage app → Logs

### "API Key Invalid"
→ Prüfe Secrets: Advanced Settings → Secrets

### "Module not found"
→ Prüfe `requirements.txt`

### "App ist langsam"
→ Normal beim ersten Start (Cold Start)

### "COBOL Installation failed"
→ Ist OK! COBOL läuft automatisch auf Streamlit Cloud

---

## 🆘 Hilfe?

**Streamlit Docs:** https://docs.streamlit.io/streamlit-community-cloud  
**Gemini Docs:** https://ai.google.dev/

---

## ✅ Checkliste

- [ ] Gemini API-Key geholt
- [ ] GitHub Repository erstellt
- [ ] Code hochgeladen
- [ ] Bei Streamlit Cloud angemeldet
- [ ] App erstellt
- [ ] Secrets hinzugefügt
- [ ] App deployed
- [ ] App getestet
- [ ] URL geteilt

---

**Viel Erfolg! 🚀**
