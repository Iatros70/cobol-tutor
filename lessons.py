"""
COBOL Lektionen und Übungen
"""

LESSONS = {
    "1_basics": {
        "title": "1. COBOL Basics - Struktur und DISPLAY",
        "description": """
        Willkommen zu deiner ersten COBOL-Lektion! 
        
        COBOL-Programme haben eine feste Struktur mit vier Hauptbereichen (DIVISIONS):
        
        1. IDENTIFICATION DIVISION - Programm-Informationen
        2. ENVIRONMENT DIVISION - Systemkonfiguration
        3. DATA DIVISION - Variablen-Definitionen
        4. PROCEDURE DIVISION - Der eigentliche Code
        
        Heute lernst du ein einfaches "Hello World" Programm zu schreiben.
        """,
        "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. HELLO.
      
      PROCEDURE DIVISION.
          DISPLAY "Hello World!".
          STOP RUN.
""",
        "exercise": {
            "task": "Schreibe ein COBOL-Programm, das deinen Namen anzeigt.",
            "hint": "Verwende DISPLAY gefolgt von Text in Anführungszeichen.",
            "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. MEINNAME.
      
      PROCEDURE DIVISION.
          DISPLAY "Mein Name ist [DEIN NAME]".
          STOP RUN.
"""
        }
    },
    
    "2_variables": {
        "title": "2. Variablen und Datentypen",
        "description": """
        In COBOL werden Variablen in der DATA DIVISION definiert.
        
        Wichtige Konzepte:
        - WORKING-STORAGE SECTION: Für normale Variablen
        - PIC (PICTURE): Definiert den Datentyp und die Größe
        - PIC 9: Numerisch
        - PIC X: Alphanumerisch (Text)
        - PIC A: Nur Buchstaben
        
        Beispiel: 01 MEIN-NAME PIC X(20) VALUE "Klaus".
        """,
        "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. VARIABLES.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 NAME PIC X(20) VALUE "Max Mustermann".
      01 ALTER PIC 99 VALUE 25.
      01 GEHALT PIC 9(5)V99 VALUE 45000.50.
      
      PROCEDURE DIVISION.
          DISPLAY "Name: " NAME.
          DISPLAY "Alter: " ALTER.
          DISPLAY "Gehalt: " GEHALT.
          STOP RUN.
""",
        "exercise": {
            "task": "Erstelle ein Programm mit drei Variablen: STADT (Text), EINWOHNER (Zahl) und JAHR (Zahl). Zeige alle drei an.",
            "hint": "Verwende PIC X für Text und PIC 9 für Zahlen. Vergiss nicht VALUE um Anfangswerte zu setzen.",
            "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. STADTINFO.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 STADT PIC X(20) VALUE "Berlin".
      01 EINWOHNER PIC 9(7) VALUE 3700000.
      01 JAHR PIC 9(4) VALUE 2025.
      
      PROCEDURE DIVISION.
          DISPLAY "Stadt: " STADT.
          DISPLAY "Einwohner: " EINWOHNER.
          DISPLAY "Jahr: " JAHR.
          STOP RUN.
"""
        }
    },
    
    "3_arithmetic": {
        "title": "3. Berechnungen und Arithmetik",
        "description": """
        COBOL bietet verschiedene Rechenbefehle:
        
        - ADD: Addition
        - SUBTRACT: Subtraktion
        - MULTIPLY: Multiplikation
        - DIVIDE: Division
        - COMPUTE: Für komplexe Formeln
        
        Syntax: ADD A TO B (addiert A zu B)
        Oder: COMPUTE C = A + B (speichert Ergebnis in C)
        """,
        "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. RECHNEN.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 ZAHL1 PIC 99 VALUE 10.
      01 ZAHL2 PIC 99 VALUE 5.
      01 ERGEBNIS PIC 999.
      
      PROCEDURE DIVISION.
          ADD ZAHL1 TO ZAHL2 GIVING ERGEBNIS.
          DISPLAY "Addition: " ERGEBNIS.
          
          COMPUTE ERGEBNIS = ZAHL1 * ZAHL2.
          DISPLAY "Multiplikation: " ERGEBNIS.
          STOP RUN.
""",
        "exercise": {
            "task": "Berechne die Fläche eines Rechtecks (Länge * Breite). Länge = 15, Breite = 8.",
            "hint": "Verwende COMPUTE oder MULTIPLY. Definiere drei Variablen.",
            "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. FLAECHE.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 LAENGE PIC 99 VALUE 15.
      01 BREITE PIC 99 VALUE 8.
      01 FLAECHE PIC 999.
      
      PROCEDURE DIVISION.
          COMPUTE FLAECHE = LAENGE * BREITE.
          DISPLAY "Flaeche: " FLAECHE.
          STOP RUN.
"""
        }
    },
    
    "4_if_statements": {
        "title": "4. IF-Bedingungen",
        "description": """
        Mit IF kannst du Entscheidungen treffen:
        
        Syntax:
        IF Bedingung
            Anweisung
        ELSE
            Andere-Anweisung
        END-IF.
        
        Vergleiche: =, >, <, >=, <=, NOT =
        """,
        "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. ALTERSCHECK.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 ALTER PIC 99 VALUE 18.
      
      PROCEDURE DIVISION.
          IF ALTER >= 18
              DISPLAY "Volljaehrig"
          ELSE
              DISPLAY "Minderjaehrig"
          END-IF.
          STOP RUN.
""",
        "exercise": {
            "task": "Schreibe ein Programm das eine Temperatur prüft: über 30 = 'Heiss', 20-30 = 'Warm', unter 20 = 'Kalt'.",
            "hint": "Verwende verschachtelte IF-Bedingungen.",
            "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. TEMPERATUR.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 TEMP PIC 99 VALUE 25.
      
      PROCEDURE DIVISION.
          IF TEMP > 30
              DISPLAY "Heiss"
          ELSE
              IF TEMP >= 20
                  DISPLAY "Warm"
              ELSE
                  DISPLAY "Kalt"
              END-IF
          END-IF.
          STOP RUN.
"""
        }
    },
    
    "5_loops": {
        "title": "5. Schleifen (PERFORM)",
        "description": """
        In COBOL verwendest du PERFORM für Schleifen:
        
        PERFORM VARYING: Zählschleife
        PERFORM UNTIL: Bedingungsschleife
        PERFORM paragraph-name: Ruft einen Absatz auf
        
        Absätze (Paragraphs) sind benannte Code-Blöcke.
        """,
        "example": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. SCHLEIFE.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 ZAEHLER PIC 99 VALUE 1.
      
      PROCEDURE DIVISION.
          PERFORM VARYING ZAEHLER FROM 1 BY 1
              UNTIL ZAEHLER > 5
              DISPLAY "Durchlauf: " ZAEHLER
          END-PERFORM.
          STOP RUN.
""",
        "exercise": {
            "task": "Erstelle das kleine 1x1 für die Zahl 7 (7x1 bis 7x10).",
            "hint": "Verwende PERFORM VARYING und COMPUTE.",
            "solution": """      IDENTIFICATION DIVISION.
      PROGRAM-ID. EINMALEINS.
      
      DATA DIVISION.
      WORKING-STORAGE SECTION.
      01 ZAEHLER PIC 99.
      01 ERGEBNIS PIC 999.
      
      PROCEDURE DIVISION.
          PERFORM VARYING ZAEHLER FROM 1 BY 1
              UNTIL ZAEHLER > 10
              COMPUTE ERGEBNIS = 7 * ZAEHLER
              DISPLAY "7 x " ZAEHLER " = " ERGEBNIS
          END-PERFORM.
          STOP RUN.
"""
        }
    }
}

def get_lesson(lesson_id):
    return LESSONS.get(lesson_id, None)

def get_all_lesson_ids():
    return list(LESSONS.keys())

def get_lesson_titles():
    return {k: v["title"] for k, v in LESSONS.items()}
