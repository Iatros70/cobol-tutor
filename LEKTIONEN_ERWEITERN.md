# 📦 COBOL-Tutor mit erweiterten Lektionen

## 🎯 Was du hier hast

Diese ZIP enthält den COBOL-Tutor mit **Basis-Version (5 Lektionen)**.

Um den **vollständigen Kurs mit 15 Lektionen** (inklusive Lotto-Generator) zu bekommen, gibt es **3 einfache Optionen**:

---

## ✅ Option 1: Erweiterte lessons.py herunterladen (EMPFOHLEN)

Die vollständige `lessons.py` mit allen 15 Lektionen ist als separate Datei verfügbar.

**So geht's:**
1. Lade die erweiterte lessons.py herunter (vom gleichen Ort wie diese ZIP)
2. Ersetze die `lessons.py` in diesem Projekt
3. Fertig!

Die Datei heißt: `lessons_15_complete.py`

---

## ⚙️ Option 2: Python-Script nutzen

Ein automatisches Script kann die Lektionen hinzufügen (teilweise).

```bash
python3 extend_lessons.py
```

**Hinweis:** Das Script fügt nur Lektion 6 hinzu als Demonstration.  
Für alle 15 Lektionen nutze Option 1 oder 3.

---

## ✍️ Option 3: Manuell erweitern

Du kannst auch selbst die Lektionen hinzufügen!

### Lektionen-Übersicht:

**Bereits vorhanden (1-5):**
1. ✅ COBOL Basics
2. ✅ Variablen  
3. ✅ Arithmetik
4. ✅ IF-Bedingungen
5. ✅ Schleifen

**Fehlend (6-15):**
6. ❌ ACCEPT (Benutzereingabe)
7. ❌ Arrays (OCCURS)
8. ❌ Zufallszahlen
9. ❌ Duplikate erkennen
10. ❌ Sortierung
11. ❌ Paragraphen
12. ❌ Einfacher Lotto-Generator
13. ❌ Lotto ohne Duplikate  
14. ❌ Lotto mit Sortierung
15. ❌ Vollständiger Lotto-Generator 🏆

### Template für neue Lektionen:

```python
"X_name": {
    "title": "X. Titel der Lektion",
    "description": """
    Beschreibung des Konzepts...
    """,
    "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. BEISPIEL.
      
      PROCEDURE DIVISION.
          DISPLAY "Beispiel-Code".
          STOP RUN.
""",
    "exercise": {
        "task": "Aufgabe für den Schüler",
        "hint": "Hilfreicher Tipp",
        "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. LOESUNG.
      
      PROCEDURE DIVISION.
          DISPLAY "Musterlösung".
          STOP RUN.
"""
    }
}
```

**Füge das in lessons.py ein** nach Lektion 5, vor dem letzten `}`.

---

## 🚀 Nach der Erweiterung

```bash
# 1. Pakete installieren
pip install -r requirements.txt

# 2. API-Key holen (kostenlos!)
# https://aistudio.google.com/app/apikey

# 3. Starten
streamlit run app.py
```

---

## 📝 Beispiel: Lektion 6 hinzufügen

Öffne `lessons.py` und füge nach Lektion 5 ein:

```python
    ,  # <- Wichtig: Komma nach Lektion 5!
    
    "6_accept": {
        "title": "6. Benutzereingabe mit ACCEPT",
        "description": """
        Mit ACCEPT kannst du Eingaben vom Benutzer entgegennehmen.
        """,
        "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. EINGABE.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 WS-NAME PIC X(30).
      
      PROCEDURE DIVISION.
          DISPLAY "Dein Name: ".
          ACCEPT WS-NAME.
          DISPLAY "Hallo " WS-NAME "!".
          STOP RUN.
""",
        "exercise": {
            "task": "Frage nach 2 Zahlen und zeige die Summe.",
            "hint": "ACCEPT zweimal, dann COMPUTE.",
            "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. SUMME.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 Z1 PIC 99.
      01 Z2 PIC 99.
      01 SUM PIC 999.
      
      PROCEDURE DIVISION.
          DISPLAY "Zahl 1: ".
          ACCEPT Z1.
          DISPLAY "Zahl 2: ".
          ACCEPT Z2.
          COMPUTE SUM = Z1 + Z2.
          DISPLAY "Summe: " SUM.
          STOP RUN.
"""
        }
    }
```

Dann wiederhole das für Lektionen 7-15.

---

## ❓ Hilfe

**lessons.py Syntax-Fehler?**
- Prüfe alle Kommas zwischen Lektionen
- Prüfe alle `"""` (drei Anführungszeichen)
- Prüfe die geschweiften Klammern `{}`

**Wo finde ich die vollständige lessons_15.py?**
- Sollte im gleichen Download-Paket sein
- Oder erstelle ein Issue im Repository

**Funktioniert der Tutor mit 5 Lektionen?**
- Ja! Du kannst sofort loslegen
- Lektionen 1-5 decken die Grundlagen ab
- Lektionen 6-15 bauen darauf auf

---

## 📚 Ressourcen

- **README.md** - Vollständige Projektdokumentation  
- **INSTALLATION.md** - Schritt-für-Schritt Installation
- **extend_lessons.py** - Automatisches Erweiterungs-Script

---

**Viel Erfolg beim Lernen! 🚀**
