"""
COBOL Lektionen und Übungen
Vollständiger Kurs: 15 Lektionen vom Anfänger zum Lotto-Generator
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
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. HELLO.

PROCEDURE DIVISION.
    DISPLAY "Hello World!".
    STOP RUN.""",
        "exercise": {
            "task": "Schreibe ein COBOL-Programm, das deinen Namen anzeigt.",
            "hint": "Verwende DISPLAY gefolgt von Text in Anführungszeichen.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. MEINNAME.

PROCEDURE DIVISION.
    DISPLAY "Mein Name ist [DEIN NAME]".
    STOP RUN."""
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
        "example": """IDENTIFICATION DIVISION.

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
    STOP RUN.""",
        "exercise": {
            "task": "Erstelle ein Programm mit drei Variablen: STADT (Text), EINWOHNER (Zahl) und JAHR (Zahl). Zeige alle drei an.",
            "hint": "Verwende PIC X für Text und PIC 9 für Zahlen. Vergiss nicht VALUE um Anfangswerte zu setzen.",
            "solution": """IDENTIFICATION DIVISION.

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
    STOP RUN."""
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
        "example": """IDENTIFICATION DIVISION.

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
    STOP RUN.""",
        "exercise": {
            "task": "Berechne die Fläche eines Rechtecks (Länge * Breite). Länge = 15, Breite = 8.",
            "hint": "Verwende COMPUTE oder MULTIPLY. Definiere drei Variablen.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. FLAECHE.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 LAENGE PIC 99 VALUE 15.
01 BREITE PIC 99 VALUE 8.
01 FLAECHE PIC 999.

PROCEDURE DIVISION.
    COMPUTE FLAECHE = LAENGE * BREITE.
    DISPLAY "Flaeche: " FLAECHE.
    STOP RUN."""
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
        "example": """IDENTIFICATION DIVISION.

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
    STOP RUN.""",
        "exercise": {
            "task": "Schreibe ein Programm das eine Temperatur prüft: über 30 = 'Heiss', 20-30 = 'Warm', unter 20 = 'Kalt'.",
            "hint": "Verwende verschachtelte IF-Bedingungen.",
            "solution": """IDENTIFICATION DIVISION.

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
    STOP RUN."""
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
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. SCHLEIFE.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 ZAEHLER PIC 99 VALUE 1.

PROCEDURE DIVISION.
    PERFORM VARYING ZAEHLER FROM 1 BY 1
    UNTIL ZAEHLER > 5
    DISPLAY "Durchlauf: " ZAEHLER
    END-PERFORM.
    STOP RUN.""",
        "exercise": {
            "task": "Erstelle das kleine 1x1 für die Zahl 7 (7x1 bis 7x10).",
            "hint": "Verwende PERFORM VARYING und COMPUTE.",
            "solution": """IDENTIFICATION DIVISION.

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
    STOP RUN."""
        }
    },
    
    "6_accept": {
        "title": "6. Benutzereingabe mit ACCEPT",
        "description": """
        Mit ACCEPT kannst du Eingaben vom Benutzer entgegennehmen:
        
        - ACCEPT variable: Liest Eingabe von der Tastatur
        - Die Eingabe wird in der angegebenen Variable gespeichert
        - Funktioniert mit allen Datentypen (Text, Zahlen)
        
        Tipp: Zeige dem Benutzer immer eine Eingabeaufforderung mit DISPLAY!
        """,
        "example": """IDENTIFICATION DIVISION.

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

    STOP RUN.""",
        "exercise": {
            "task": "Erstelle ein Programm, das nach zwei Zahlen fragt und deren Summe berechnet und anzeigt.",
            "hint": "Verwende ACCEPT für beide Zahlen und COMPUTE oder ADD für die Summe.",
            "solution": """IDENTIFICATION DIVISION.

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
    STOP RUN."""
        }
    },
    
    "7_arrays": {
        "title": "7. Arrays mit OCCURS",
        "description": """
        Arrays (Tabellen) in COBOL:
        
        - OCCURS n TIMES: Definiert ein Array mit n Elementen
        - Zugriff über Index: variable(1), variable(2), ...
        - Indizes beginnen bei 1 (nicht bei 0!)
        - Perfekt für Listen von Zahlen oder Texten
        
        Arrays werden oft mit PERFORM VARYING durchlaufen.
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. ARRAYS.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN-TABELLE.
    05 WS-ZAHL PIC 99 OCCURS 5 TIMES.
01 WS-INDEX PIC 9 VALUE 1.

PROCEDURE DIVISION.
    MOVE 10 TO WS-ZAHL(1).
    MOVE 20 TO WS-ZAHL(2).
    MOVE 30 TO WS-ZAHL(3).
    MOVE 40 TO WS-ZAHL(4).
    MOVE 50 TO WS-ZAHL(5).

    DISPLAY "Ausgabe aller Werte:".
    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 5
    DISPLAY "Position " WS-INDEX ": " WS-ZAHL(WS-INDEX)
    END-PERFORM.

    STOP RUN.""",
        "exercise": {
            "task": "Erstelle ein Array mit 4 Zahlen. Lass den Benutzer alle 4 Zahlen eingeben und zeige dann den Durchschnitt an.",
            "hint": "Verwende OCCURS 4 TIMES, eine Schleife für ACCEPT und berechne die Summe/4.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. DURCHSCHNITT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 4 TIMES.
01 WS-INDEX PIC 9.
01 WS-SUMME PIC 999 VALUE 0.
01 WS-DURCHSCHNITT PIC 99V99.

PROCEDURE DIVISION.
    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 4
    DISPLAY "Zahl " WS-INDEX ": "
    ACCEPT WS-ZAHL(WS-INDEX)
    ADD WS-ZAHL(WS-INDEX) TO WS-SUMME
    END-PERFORM.

    COMPUTE WS-DURCHSCHNITT = WS-SUMME / 4.
    DISPLAY "Durchschnitt: " WS-DURCHSCHNITT.
    STOP RUN."""
        }
    },
    
    "8_random": {
        "title": "8. Zufallszahlen generieren",
        "description": """
        Zufallszahlen mit FUNCTION RANDOM:
        
        - FUNCTION RANDOM gibt eine Zahl zwischen 0.0000 und 0.9999 zurück
        - Um Zahlen in einem Bereich zu bekommen: (RANDOM * Bereich) + Start
        - Beispiel für 1-49: (RANDOM * 49) + 1
        
        Die COMPUTE-Anweisung wird für Berechnungen verwendet.
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. ZUFALL.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZUFALLSZAHL PIC 9V9999.
01 WS-ZAHL PIC 99.
01 WS-ZAEHLER PIC 99.

PROCEDURE DIVISION.
    DISPLAY "10 Zufallszahlen zwischen 1 und 49:".
    PERFORM VARYING WS-ZAEHLER FROM 1 BY 1 
    UNTIL WS-ZAEHLER > 10
    COMPUTE WS-ZUFALLSZAHL = FUNCTION RANDOM
    COMPUTE WS-ZAHL = (WS-ZUFALLSZAHL * 49) + 1
    DISPLAY "Zahl " WS-ZAEHLER ": " WS-ZAHL
    END-PERFORM.

    STOP RUN.""",
        "exercise": {
            "task": "Erstelle ein Würfel-Simulator, der 5 mal würfelt (Zufallszahlen 1-6) und alle Ergebnisse anzeigt.",
            "hint": "Formel für 1-6: (RANDOM * 6) + 1. Verwende eine PERFORM-Schleife.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. WUERFEL.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZUFALL PIC 9V9999.
01 WS-WURF PIC 9.
01 WS-ZAEHLER PIC 9.

PROCEDURE DIVISION.
    DISPLAY "Wuerfeln (5 Wuerfe):".
    PERFORM VARYING WS-ZAEHLER FROM 1 BY 1 
    UNTIL WS-ZAEHLER > 5
    COMPUTE WS-ZUFALL = FUNCTION RANDOM
    COMPUTE WS-WURF = (WS-ZUFALL * 6) + 1
    DISPLAY "Wurf " WS-ZAEHLER ": " WS-WURF
    END-PERFORM.
    STOP RUN."""
        }
    },
    
    "9_duplicates": {
        "title": "9. Duplikate erkennen",
        "description": """
        Duplikate in Arrays finden:
        
        - Verwende verschachtelte Schleifen
        - Äußere Schleife: Jedes Element
        - Innere Schleife: Vergleiche mit allen anderen Elementen
        - Wichtig: Innere Schleife startet bei Index+1
        
        Ein Flag (0/1) hilft beim Merken, ob Duplikate gefunden wurden.
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. DUPLIKATE.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN-TABELLE.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-INDEX-I PIC 9.
01 WS-INDEX-J PIC 9.
01 WS-GEFUNDEN PIC 9 VALUE 0.

PROCEDURE DIVISION.
    DISPLAY "Gib 6 Zahlen ein (1-49):".
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 6
    DISPLAY "Zahl " WS-INDEX-I ": "
    ACCEPT WS-ZAHL(WS-INDEX-I)
    END-PERFORM.

    MOVE 0 TO WS-GEFUNDEN.
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 5
    PERFORM VARYING WS-INDEX-J FROM WS-INDEX-I + 1 BY 1
    UNTIL WS-INDEX-J > 6
    IF WS-ZAHL(WS-INDEX-I) = WS-ZAHL(WS-INDEX-J)
    DISPLAY "Duplikat: " WS-ZAHL(WS-INDEX-I)
    MOVE 1 TO WS-GEFUNDEN
    END-IF
    END-PERFORM
    END-PERFORM.

    IF WS-GEFUNDEN = 0
    DISPLAY "Keine Duplikate!"
    END-IF.
    STOP RUN.""",
        "exercise": {
            "task": "Erstelle ein Programm mit 5 Zahlen. Prüfe, ob die Zahl 42 vorhanden ist und gib eine entsprechende Meldung aus.",
            "hint": "Brauchst nur eine einfache Schleife und ein IF für den Vergleich mit 42.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. SUCHE42.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 5 TIMES.
01 WS-INDEX PIC 9.
01 WS-GEFUNDEN PIC 9 VALUE 0.

PROCEDURE DIVISION.
    DISPLAY "Gib 5 Zahlen ein:".
    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 5
    ACCEPT WS-ZAHL(WS-INDEX)
    END-PERFORM.

    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 5
    IF WS-ZAHL(WS-INDEX) = 42
    MOVE 1 TO WS-GEFUNDEN
    EXIT PERFORM
    END-IF
    END-PERFORM.

    IF WS-GEFUNDEN = 1
    DISPLAY "42 gefunden!"
    ELSE
    DISPLAY "42 nicht gefunden."
    END-IF.
    STOP RUN."""
        }
    },
    
    "10_sorting": {
        "title": "10. Bubble-Sort Sortierung",
        "description": """
        Zahlen sortieren mit Bubble-Sort:
        
        - Klassischer Sortieralgorithmus
        - Vergleicht benachbarte Elemente
        - Tauscht sie, wenn sie falsch sortiert sind
        - Wiederholt dies, bis alles sortiert ist
        
        Braucht eine temporäre Variable zum Tauschen!
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. SORTIEREN.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN-TABELLE.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-INDEX-I PIC 9.
01 WS-INDEX-J PIC 9.
01 WS-TEMP PIC 99.
01 WS-GETAUSCHT PIC 9.

PROCEDURE DIVISION.
    DISPLAY "Gib 6 Zahlen ein:".
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 6
    ACCEPT WS-ZAHL(WS-INDEX-I)
    END-PERFORM.

    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 5
    MOVE 0 TO WS-GETAUSCHT
    PERFORM VARYING WS-INDEX-J FROM 1 BY 1
    UNTIL WS-INDEX-J > 6 - WS-INDEX-I
    IF WS-ZAHL(WS-INDEX-J) > 
    WS-ZAHL(WS-INDEX-J + 1)
    MOVE WS-ZAHL(WS-INDEX-J) TO WS-TEMP
    MOVE WS-ZAHL(WS-INDEX-J + 1) 
    TO WS-ZAHL(WS-INDEX-J)
    MOVE WS-TEMP TO WS-ZAHL(WS-INDEX-J + 1)
    MOVE 1 TO WS-GETAUSCHT
    END-IF
    END-PERFORM
    IF WS-GETAUSCHT = 0
    EXIT PERFORM
    END-IF
    END-PERFORM.

    DISPLAY "Sortierte Liste:".
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 6
    DISPLAY WS-ZAHL(WS-INDEX-I)
    END-PERFORM.
    STOP RUN.""",
        "exercise": {
            "task": "Sortiere 4 Zahlen in absteigender Reihenfolge (größte zuerst).",
            "hint": "Ändere einfach das > zu < im Vergleich!",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. SORTABST.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 4 TIMES.
01 WS-I PIC 9.
01 WS-J PIC 9.
01 WS-TEMP PIC 99.

PROCEDURE DIVISION.
    DISPLAY "Gib 4 Zahlen ein:".
    PERFORM VARYING WS-I FROM 1 BY 1 
    UNTIL WS-I > 4
    ACCEPT WS-ZAHL(WS-I)
    END-PERFORM.

    PERFORM VARYING WS-I FROM 1 BY 1 
    UNTIL WS-I > 3
    PERFORM VARYING WS-J FROM 1 BY 1
    UNTIL WS-J > 4 - WS-I
    IF WS-ZAHL(WS-J) < WS-ZAHL(WS-J + 1)
    MOVE WS-ZAHL(WS-J) TO WS-TEMP
    MOVE WS-ZAHL(WS-J + 1) TO WS-ZAHL(WS-J)
    MOVE WS-TEMP TO WS-ZAHL(WS-J + 1)
    END-IF
    END-PERFORM
    END-PERFORM.

    DISPLAY "Absteigend sortiert:".
    PERFORM VARYING WS-I FROM 1 BY 1 
    UNTIL WS-I > 4
    DISPLAY WS-ZAHL(WS-I)
    END-PERFORM.
    STOP RUN."""
        }
    },
    
    "11_paragraphs": {
        "title": "11. Strukturierte Programmierung mit Paragraphen",
        "description": """
        Paragraphen organisieren Code:
        
        - Benannte Code-Blöcke
        - Aufruf mit PERFORM paragraph-name
        - Machen Programme übersichtlicher
        - Wie Funktionen in anderen Sprachen
        
        Paragraph-Namen stehen linksbündig (Area A) und enden mit einem Punkt.
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. PARAGRAPHEN.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHL PIC 99 VALUE 10.

PROCEDURE DIVISION.
MAIN-LOGIC.
    DISPLAY "Programm Start".
    PERFORM ZEIGE-INFO.
    PERFORM RECHNE.
    DISPLAY "Programm Ende".
    STOP RUN.

ZEIGE-INFO.
    DISPLAY "=== Info ===".
    DISPLAY "Dies ist ein Beispiel".

RECHNE.
    DISPLAY "=== Rechnung ===".
    COMPUTE WS-ZAHL = WS-ZAHL * 2.
    DISPLAY "Ergebnis: " WS-ZAHL.""",
        "exercise": {
            "task": "Erstelle ein Menü-Programm mit drei Paragraphen: ZEIGE-MENU, OPTION-A und OPTION-B. ZEIGE-MENU ruft die anderen auf.",
            "hint": "Jeder Paragraph braucht einen Namen und kann mit PERFORM aufgerufen werden.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. MENU.

PROCEDURE DIVISION.
MAIN-LOGIC.
    PERFORM ZEIGE-MENU.
    STOP RUN.

ZEIGE-MENU.
    DISPLAY "=== HAUPTMENU ===".
    DISPLAY "Fuehre alle Optionen aus:".
    PERFORM OPTION-A.
    PERFORM OPTION-B.

OPTION-A.
    DISPLAY "Option A ausgefuehrt".

OPTION-B.
    DISPLAY "Option B ausgefuehrt"."""
        }
    },
    
    "12_lotto_basic": {
        "title": "12. Einfacher Lotto-Generator",
        "description": """
        Kombinieren wir alles für einen einfachen Lotto-Generator:
        
        - 6 Zufallszahlen zwischen 1 und 49
        - Ohne Duplikat-Prüfung (kommt später!)
        - Zeige alle generierten Zahlen an
        
        Dies ist der erste Schritt zum vollständigen Lotto-Programm.
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTOEINFACH.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-INDEX PIC 9.
01 WS-ZUFALL PIC 9V9999.

PROCEDURE DIVISION.
    DISPLAY "=== LOTTO 6 aus 49 ===".

    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 6
    COMPUTE WS-ZUFALL = FUNCTION RANDOM
    COMPUTE WS-ZAHL(WS-INDEX) = (WS-ZUFALL * 49) + 1
    END-PERFORM.

    DISPLAY "Deine Zahlen:".
    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 6
    DISPLAY "  " WS-ZAHL(WS-INDEX)
    END-PERFORM.

    STOP RUN.""",
        "exercise": {
            "task": "Ändere das Programm für 'Eurojackpot': 5 aus 50 Zahlen.",
            "hint": "Ändere OCCURS auf 5 und die Formel auf (RANDOM * 50) + 1.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. EUROJACKPOT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 5 TIMES.
01 WS-INDEX PIC 9.
01 WS-ZUFALL PIC 9V9999.

PROCEDURE DIVISION.
    DISPLAY "=== EUROJACKPOT 5 aus 50 ===".

    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 5
    COMPUTE WS-ZUFALL = FUNCTION RANDOM
    COMPUTE WS-ZAHL(WS-INDEX) = (WS-ZUFALL * 50) + 1
    END-PERFORM.

    DISPLAY "Deine Zahlen:".
    PERFORM VARYING WS-INDEX FROM 1 BY 1 
    UNTIL WS-INDEX > 5
    DISPLAY "  " WS-ZAHL(WS-INDEX)
    END-PERFORM.
    STOP RUN."""
        }
    },
    
    "13_lotto_nodups": {
        "title": "13. Lotto ohne Duplikate",
        "description": """
        Jetzt verbessern wir den Generator:
        
        - Generiere Zufallszahlen
        - Prüfe vor dem Hinzufügen auf Duplikate
        - Nur einzigartige Zahlen speichern
        - Wiederhole bis 6 verschiedene Zahlen gefunden
        
        Wir verwenden PERFORM UNTIL und eine Duplikat-Prüfung!
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTOUNIQUE.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-LOTTO-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-ZUFALLSWERT PIC 9V9999.
01 WS-NEUE-ZAHL PIC 99.
01 WS-ANZAHL PIC 9 VALUE 0.
01 WS-INDEX-I PIC 9.
01 WS-DUPLIKAT PIC 9.

PROCEDURE DIVISION.
MAIN-LOGIC.
    DISPLAY "=== LOTTO 6 aus 49 (ohne Duplikate) ===".

    PERFORM UNTIL WS-ANZAHL = 6
    COMPUTE WS-ZUFALLSWERT = FUNCTION RANDOM
    COMPUTE WS-NEUE-ZAHL = (WS-ZUFALLSWERT * 49) + 1

    PERFORM PRUEFE-DUPLIKAT

    IF WS-DUPLIKAT = 0
    ADD 1 TO WS-ANZAHL
    MOVE WS-NEUE-ZAHL TO WS-ZAHL(WS-ANZAHL)
    END-IF
    END-PERFORM.

    DISPLAY "Deine Zahlen:".
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 6
    DISPLAY "  " WS-ZAHL(WS-INDEX-I)
    END-PERFORM.
    STOP RUN.

PRUEFE-DUPLIKAT.
    MOVE 0 TO WS-DUPLIKAT.
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > WS-ANZAHL
    IF WS-NEUE-ZAHL = WS-ZAHL(WS-INDEX-I)
    MOVE 1 TO WS-DUPLIKAT
    EXIT PERFORM
    END-IF
    END-PERFORM.""",
        "exercise": {
            "task": "Zähle, wie viele Versuche nötig waren, um 6 verschiedene Zahlen zu finden.",
            "hint": "Füge eine Zähler-Variable hinzu, die bei jedem generierten Wert erhöht wird.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTOCOUNT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-ZUFALL PIC 9V9999.
01 WS-NEU PIC 99.
01 WS-ANZ PIC 9 VALUE 0.
01 WS-VERSUCHE PIC 99 VALUE 0.
01 WS-I PIC 9.
01 WS-DUP PIC 9.

PROCEDURE DIVISION.
    PERFORM UNTIL WS-ANZ = 6
    COMPUTE WS-ZUFALL = FUNCTION RANDOM
    COMPUTE WS-NEU = (WS-ZUFALL * 49) + 1
    ADD 1 TO WS-VERSUCHE

    MOVE 0 TO WS-DUP
    PERFORM VARYING WS-I FROM 1 BY 1 
    UNTIL WS-I > WS-ANZ
    IF WS-NEU = WS-ZAHL(WS-I)
    MOVE 1 TO WS-DUP
    END-IF
    END-PERFORM

    IF WS-DUP = 0
    ADD 1 TO WS-ANZ
    MOVE WS-NEU TO WS-ZAHL(WS-ANZ)
    END-IF
    END-PERFORM.

    DISPLAY "Versuche: " WS-VERSUCHE.
    DISPLAY "Zahlen:".
    PERFORM VARYING WS-I FROM 1 BY 1 
    UNTIL WS-I > 6
    DISPLAY "  " WS-ZAHL(WS-I)
    END-PERFORM.
    STOP RUN."""
        }
    },
    
    "14_lotto_sorted": {
        "title": "14. Lotto mit Sortierung",
        "description": """
        Komplettieren wir den Generator:
        
        - Generiere 6 einzigartige Zahlen
        - Sortiere sie aufsteigend
        - Schöne, übersichtliche Ausgabe
        
        Kombiniert Zufallszahlen, Duplikat-Prüfung und Bubble-Sort!
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTOSORT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-LOTTO-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-ZUFALLSWERT PIC 9V9999.
01 WS-NEUE-ZAHL PIC 99.
01 WS-ANZAHL PIC 9 VALUE 0.
01 WS-INDEX-I PIC 9.
01 WS-INDEX-J PIC 9.
01 WS-DUPLIKAT PIC 9.
01 WS-TEMP PIC 99.

PROCEDURE DIVISION.
MAIN-LOGIC.
    DISPLAY "=== LOTTO 6 aus 49 ===".
    PERFORM GENERIERE-ZAHLEN.
    PERFORM SORTIERE-ZAHLEN.
    PERFORM ZEIGE-ERGEBNIS.
    STOP RUN.

GENERIERE-ZAHLEN.
    PERFORM UNTIL WS-ANZAHL = 6
    COMPUTE WS-ZUFALLSWERT = FUNCTION RANDOM
    COMPUTE WS-NEUE-ZAHL = (WS-ZUFALLSWERT * 49) + 1
    PERFORM PRUEFE-DUPLIKAT
    IF WS-DUPLIKAT = 0
    ADD 1 TO WS-ANZAHL
    MOVE WS-NEUE-ZAHL TO WS-ZAHL(WS-ANZAHL)
    END-IF
    END-PERFORM.

PRUEFE-DUPLIKAT.
    MOVE 0 TO WS-DUPLIKAT.
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > WS-ANZAHL
    IF WS-NEUE-ZAHL = WS-ZAHL(WS-INDEX-I)
    MOVE 1 TO WS-DUPLIKAT
    EXIT PERFORM
    END-IF
    END-PERFORM.

SORTIERE-ZAHLEN.
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 5
    PERFORM VARYING WS-INDEX-J FROM 1 BY 1
    UNTIL WS-INDEX-J > 6 - WS-INDEX-I
    IF WS-ZAHL(WS-INDEX-J) > 
    WS-ZAHL(WS-INDEX-J + 1)
    MOVE WS-ZAHL(WS-INDEX-J) TO WS-TEMP
    MOVE WS-ZAHL(WS-INDEX-J + 1) 
    TO WS-ZAHL(WS-INDEX-J)
    MOVE WS-TEMP TO WS-ZAHL(WS-INDEX-J + 1)
    END-IF
    END-PERFORM
    END-PERFORM.

ZEIGE-ERGEBNIS.
    DISPLAY "Deine Lottozahlen:".
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 6
    DISPLAY "  " WS-ZAHL(WS-INDEX-I)
    END-PERFORM.""",
        "exercise": {
            "task": "Füge eine Superzahl (0-9) hinzu, die am Ende angezeigt wird.",
            "hint": "Generiere eine weitere Zufallszahl mit (RANDOM * 10), keine Duplikat-Prüfung nötig.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTOSUPER.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-SUPERZAHL PIC 9.
01 WS-ZUFALL PIC 9V9999.
01 WS-NEU PIC 99.
01 WS-ANZ PIC 9 VALUE 0.
01 WS-I PIC 9.
01 WS-J PIC 9.
01 WS-DUP PIC 9.
01 WS-TEMP PIC 99.

PROCEDURE DIVISION.
    PERFORM UNTIL WS-ANZ = 6
    COMPUTE WS-ZUFALL = FUNCTION RANDOM
    COMPUTE WS-NEU = (WS-ZUFALL * 49) + 1
    MOVE 0 TO WS-DUP
    PERFORM VARYING WS-I FROM 1 BY 1 
    UNTIL WS-I > WS-ANZ
    IF WS-NEU = WS-ZAHL(WS-I)
    MOVE 1 TO WS-DUP
    END-IF
    END-PERFORM
    IF WS-DUP = 0
    ADD 1 TO WS-ANZ
    MOVE WS-NEU TO WS-ZAHL(WS-ANZ)
    END-IF
    END-PERFORM.

    PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 5
    PERFORM VARYING WS-J FROM 1 BY 1
    UNTIL WS-J > 6 - WS-I
    IF WS-ZAHL(WS-J) > WS-ZAHL(WS-J + 1)
    MOVE WS-ZAHL(WS-J) TO WS-TEMP
    MOVE WS-ZAHL(WS-J + 1) TO WS-ZAHL(WS-J)
    MOVE WS-TEMP TO WS-ZAHL(WS-J + 1)
    END-IF
    END-PERFORM
    END-PERFORM.

    COMPUTE WS-ZUFALL = FUNCTION RANDOM.
    COMPUTE WS-SUPERZAHL = WS-ZUFALL * 10.

    DISPLAY "Zahlen:".
    PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 6
    DISPLAY "  " WS-ZAHL(WS-I)
    END-PERFORM.
    DISPLAY "Superzahl: " WS-SUPERZAHL.
    STOP RUN."""
        }
    },
    
    "15_lotto_complete": {
        "title": "15. Vollständiger Lotto-Generator 🎓",
        "description": """
        Das Finale: Professioneller Lotto-Generator!
        
        Features:
        - 6 aus 49 mit Duplikat-Prüfung
        - Sortierte Ausgabe
        - Schönes Layout
        - Option für neue Zahlen
        - Strukturierte Paragraphen
        
        Dies ist dein Meisterstück! 🏆
        """,
        "example": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-LOTTO-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-ZUFALLSWERT PIC 9V9999.
01 WS-NEUE-ZAHL PIC 99.
01 WS-ANZAHL PIC 9 VALUE 0.
01 WS-INDEX-I PIC 9.
01 WS-INDEX-J PIC 9.
01 WS-DUPLIKAT PIC 9.
01 WS-TEMP PIC 99.
01 WS-GETAUSCHT PIC 9.
01 WS-WEITER PIC X.

PROCEDURE DIVISION.
MAIN-LOGIC.
    PERFORM ZEIGE-TITEL.
    PERFORM GENERIERE-LOTTO-ZAHLEN.
    PERFORM SORTIERE-LOTTO-ZAHLEN.
    PERFORM ZEIGE-ERGEBNIS.
    PERFORM FRAGE-WEITER.

    IF WS-WEITER = "J" OR WS-WEITER = "j"
    GO TO MAIN-LOGIC
    END-IF.

    DISPLAY "Viel Glueck!".
    STOP RUN.

ZEIGE-TITEL.
    DISPLAY "********************************".
    DISPLAY "*   LOTTO 6 aus 49 GENERATOR  *".
    DISPLAY "********************************".

GENERIERE-LOTTO-ZAHLEN.
    MOVE 0 TO WS-ANZAHL.

    PERFORM UNTIL WS-ANZAHL = 6
    COMPUTE WS-ZUFALLSWERT = FUNCTION RANDOM
    COMPUTE WS-NEUE-ZAHL = (WS-ZUFALLSWERT * 49) + 1

    PERFORM PRUEFE-DUPLIKAT

    IF WS-DUPLIKAT = 0
    ADD 1 TO WS-ANZAHL
    MOVE WS-NEUE-ZAHL TO WS-ZAHL(WS-ANZAHL)
    END-IF
    END-PERFORM.

PRUEFE-DUPLIKAT.
    MOVE 0 TO WS-DUPLIKAT.
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > WS-ANZAHL
    IF WS-NEUE-ZAHL = WS-ZAHL(WS-INDEX-I)
    MOVE 1 TO WS-DUPLIKAT
    EXIT PERFORM
    END-IF
    END-PERFORM.

SORTIERE-LOTTO-ZAHLEN.
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 5
    MOVE 0 TO WS-GETAUSCHT
    PERFORM VARYING WS-INDEX-J FROM 1 BY 1
    UNTIL WS-INDEX-J > 6 - WS-INDEX-I
    IF WS-ZAHL(WS-INDEX-J) > 
    WS-ZAHL(WS-INDEX-J + 1)
    MOVE WS-ZAHL(WS-INDEX-J) TO WS-TEMP
    MOVE WS-ZAHL(WS-INDEX-J + 1) 
    TO WS-ZAHL(WS-INDEX-J)
    MOVE WS-TEMP TO WS-ZAHL(WS-INDEX-J + 1)
    MOVE 1 TO WS-GETAUSCHT
    END-IF
    END-PERFORM
    IF WS-GETAUSCHT = 0
    EXIT PERFORM
    END-IF
    END-PERFORM.

ZEIGE-ERGEBNIS.
    DISPLAY " ".
    DISPLAY "Deine Lottozahlen:".
    DISPLAY "-------------------".
    PERFORM VARYING WS-INDEX-I FROM 1 BY 1 
    UNTIL WS-INDEX-I > 6
    DISPLAY "  " WS-ZAHL(WS-INDEX-I)
    END-PERFORM.
    DISPLAY "-------------------".

FRAGE-WEITER.
    DISPLAY " ".
    DISPLAY "Neue Zahlen? (J/N): ".
    ACCEPT WS-WEITER.""",
        "exercise": {
            "task": "Erweitere das Programm um eine Statistik: Zähle, wie oft jede Zahl 1-49 insgesamt generiert wurde (über mehrere Durchläufe).",
            "hint": "Brauchst ein zweites Array mit 49 Elementen als Zähler. Erhöhe bei jeder generierten Zahl den entsprechenden Zähler.",
            "solution": """IDENTIFICATION DIVISION.

PROGRAM-ID. LOTTOSTAT.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-ZAHLEN.
    05 WS-ZAHL PIC 99 OCCURS 6 TIMES.
01 WS-STATISTIK.
    05 WS-COUNT PIC 999 OCCURS 49 TIMES VALUE 0.
01 WS-ZUFALL PIC 9V9999.
01 WS-NEU PIC 99.
01 WS-ANZ PIC 9.
01 WS-I PIC 99.
01 WS-J PIC 9.
01 WS-DUP PIC 9.
01 WS-TEMP PIC 99.
01 WS-WEITER PIC X.

PROCEDURE DIVISION.
HAUPT.
    MOVE 0 TO WS-ANZ
    PERFORM UNTIL WS-ANZ = 6
    COMPUTE WS-ZUFALL = FUNCTION RANDOM
    COMPUTE WS-NEU = (WS-ZUFALL * 49) + 1
    MOVE 0 TO WS-DUP
    PERFORM VARYING WS-J FROM 1 BY 1 
    UNTIL WS-J > WS-ANZ
    IF WS-NEU = WS-ZAHL(WS-J)
    MOVE 1 TO WS-DUP
    END-IF
    END-PERFORM
    IF WS-DUP = 0
    ADD 1 TO WS-ANZ
    MOVE WS-NEU TO WS-ZAHL(WS-ANZ)
    ADD 1 TO WS-COUNT(WS-NEU)
    END-IF
    END-PERFORM.

    PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 5
    PERFORM VARYING WS-J FROM 1 BY 1
    UNTIL WS-J > 6 - WS-I
    IF WS-ZAHL(WS-J) > WS-ZAHL(WS-J + 1)
    MOVE WS-ZAHL(WS-J) TO WS-TEMP
    MOVE WS-ZAHL(WS-J + 1) TO WS-ZAHL(WS-J)
    MOVE WS-TEMP TO WS-ZAHL(WS-J + 1)
    END-IF
    END-PERFORM
    END-PERFORM.

    DISPLAY "Zahlen:".
    PERFORM VARYING WS-J FROM 1 BY 1 UNTIL WS-J > 6
    DISPLAY "  " WS-ZAHL(WS-J)
    END-PERFORM.

    DISPLAY " ".
    DISPLAY "Neue Zahlen? (J/N): ".
    ACCEPT WS-WEITER.
    IF WS-WEITER = "J" OR WS-WEITER = "j"
    GO TO HAUPT
    END-IF.

    DISPLAY " ".
    DISPLAY "=== STATISTIK ===".
    PERFORM VARYING WS-I FROM 1 BY 1 UNTIL WS-I > 49
    IF WS-COUNT(WS-I) > 0
    DISPLAY "Zahl " WS-I ": " 
    WS-COUNT(WS-I) " mal"
    END-IF
    END-PERFORM.
    STOP RUN."""
        }
    }
}

def get_lesson(lesson_id):
    return LESSONS.get(lesson_id, None)

def get_all_lesson_ids():
    return list(LESSONS.keys())

def get_lesson_titles():
    return {k: v["title"] for k, v in LESSONS.items()}
