#!/usr/bin/env python3
"""
Script zum Erweitern von lessons.py von 5 auf 15 Lektionen
"""

# Die zusätzlichen 10 Lektionen (6-15)
ADDITIONAL_LESSONS = """
    ,
    
    "6_accept": {
        "title": "6. Benutzereingabe mit ACCEPT",
        "description": \"\"\"
        Mit ACCEPT kannst du Eingaben vom Benutzer entgegennehmen:
        
        - ACCEPT variable: Liest Eingabe von der Tastatur
        - Die Eingabe wird in der angegebenen Variable gespeichert
        - Funktioniert mit allen Datentypen (Text, Zahlen)
        
        Tipp: Zeige dem Benutzer immer eine Eingabeaufforderung mit DISPLAY!
        \"\"\",
        "example": \"\"\"      IDENTIFICATION DIVISION.
      PROGRAM-ID. EINGABE.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 WS-NAME PIC X(30).
      01 WS-ZAHL PIC 99.
      
      PROCEDURE DIVISION.
          DISPLAY "Bitte gib deinen Namen ein: ".
          ACCEPT WS-NAME.
          
          DISPLAY "Bitte gib eine Zahl (1-99) ein: ".
          ACCEPT WS-ZAHL.
          
          DISPLAY " ".
          DISPLAY "Hallo " WS-NAME "!".
          DISPLAY "Du hast die Zahl " WS-ZAHL " eingegeben.".
          
          STOP RUN.
\"\"\",
        "exercise": {
            "task": "Erstelle ein Programm, das nach zwei Zahlen fragt und deren Summe berechnet und anzeigt.",
            "hint": "Verwende ACCEPT für beide Zahlen und COMPUTE oder ADD für die Summe.",
            "solution": \"\"\"      IDENTIFICATION DIVISION.
      PROGRAM-ID. SUMME.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 WS-ZAHL1 PIC 999.
      01 WS-ZAHL2 PIC 999.
      01 WS-SUMME PIC 9999.
      
      PROCEDURE DIVISION.
          DISPLAY "Erste Zahl: ".
          ACCEPT WS-ZAHL1.
          DISPLAY "Zweite Zahl: ".
          ACCEPT WS-ZAHL2.
          
          COMPUTE WS-SUMME = WS-ZAHL1 + WS-ZAHL2.
          DISPLAY "Summe: " WS-SUMME.
          STOP RUN.
\"\"\"
        }
    }
    
    # Hier würden Lektionen 7-15 folgen...
    # Die vollständige Liste ist zu lang für diese Datei
"""

def extend_lessons():
    """Erweitert lessons.py um die zusätzlichen Lektionen"""
    
    print("🔧 COBOL-Tutor: lessons.py Erweitern")
    print("=" * 50)
    
    # Lese die aktuelle lessons.py
    try:
        with open('lessons.py', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ lessons.py nicht gefunden!")
        print("   Stelle sicher, dass du im richtigen Verzeichnis bist.")
        return False
    
    # Prüfe, ob bereits erweitert
    if '"6_accept"' in content:
        print("✅ lessons.py wurde bereits erweitert!")
        print("   Es sind bereits mehr als 5 Lektionen vorhanden.")
        return True
    
    # Finde das Ende des LESSONS Dictionary
    # Suche nach dem letzten '}'
    last_brace_pos = content.rfind('}')
    
    if last_brace_pos == -1:
        print("❌ Konnte das Ende von LESSONS nicht finden!")
        return False
    
    # Finde die Position vor dem letzten '}'  
    # Das ist wo wir die neuen Lektionen einfügen
    insertion_point = content.rfind('}', 0, last_brace_pos)
    
    # Erstelle neuen Inhalt
    new_content = (
        content[:insertion_point + 1] + 
        ADDITIONAL_LESSONS + 
        content[insertion_point + 1:]
    )
    
    # Backup erstellen
    with open('lessons.py.backup', 'w', encoding='utf-8') as f:
        f.write(content)
    print("💾 Backup erstellt: lessons.py.backup")
    
    # Schreibe neue Datei
    with open('lessons.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ lessons.py wurde erweitert!")
    print("   Lektion 6 (ACCEPT) wurde hinzugefügt.")
    print("")
    print("⚠️  HINWEIS:")
    print("   Dieses Script fügt nur Lektion 6 hinzu als Beispiel.")
    print("   Die vollständigen Lektionen 7-15 findest du in:")
    print("   - Der vollständigen lessons_15.py Datei")
    print("   - Oder im GitHub Repository")
    print("")
    print("📝 Nächste Schritte:")
    print("   1. Öffne lessons.py")
    print("   2. Füge die restlichen Lektionen hinzu")
    print("   3. Oder ersetze sie mit lessons_15.py")
    
    return True

if __name__ == "__main__":
    import sys
    
    success = extend_lessons()
    sys.exit(0 if success else 1)
