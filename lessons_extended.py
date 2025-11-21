"""
COBOL Lektionen und Übungen - ERWEITERTE VERSION mit 15 Lektionen
"""

# Importiere die Basislektionen
from typing import Dict, Any

LESSONS: Dict[str, Dict[str, Any]] = {}

# Lektionen 1-5 (Original)
LESSONS["1_basics"] = {
    "title": "1. COBOL Basics - Struktur und DISPLAY",
    "description": "Willkommen zu deiner ersten COBOL-Lektion! COBOL-Programme haben eine feste Struktur mit vier Hauptbereichen (DIVISIONS).",
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
          DISPLAY "Mein Name ist Ernst".
          STOP RUN.
"""
    }
}
