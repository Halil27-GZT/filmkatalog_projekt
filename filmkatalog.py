# Hauptcode für Filmkatalog
# Dein Filmkatalog-Programm

filme = {} # Ein Dictionary zum Speichern der Filme. Schlüssel: Filmtitel, Wert: Dictionary mit Details

def filme_anzeigen():
    if not filme:
        print("Der Katalog ist leer.")
        return

    print("\n--- Dein Filmkatalog ---")
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

def film_hinzufuegen():
    print("\n--- Film hinzufügen ---")
    titel = input("Titel des Films: ")
    regisseur = input("Regisseur des Films: ")
    jahr = input("Erscheinungsjahr des Films: ")

    if titel in filme:
        print(f"Fehler: Film '{titel}' existiert bereits im Katalog.")
        return

    filme[titel] = {
        "regisseur": regisseur,
        "jahr": jahr
    }
    print(f"Film '{titel}' wurde hinzugefügt.")

def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Beenden")
    print("------------------------")
    
def main():
    while True: # Eine Endlosschleife für das Menü
        zeige_menue() # Zeige das Menü an
        wahl = input("Ihre Wahl: ") # Erfasse die Benutzereingabe

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            print("Programm wird beendet. Auf Wiedersehen!")
            break # Beende die Schleife und damit das Programm
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")
if __name__ == "__main__":
    main() # Starte das Programm
# Test der Funktionen (werden später durch ein Menü ersetzt)
film_hinzufuegen()
filme_anzeigen()

