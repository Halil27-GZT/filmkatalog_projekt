import json
# Hauptcode für Filmkatalog
# Dein Filmkatalog-Programm

filme = {} # Ein Dictionary zum Speichern der Filme. Schlüssel: Filmtitel, Wert: Dictionary mit Details
DATEINAME = "filme.json" # Dateiname für die Speicherung des Katalogs

def filme_anzeigen():
    if not filme:
        print("Der Katalog ist leer.")
        return

    print("\n--- Dein Filmkatalog ---")
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print(f"  Genre: {details.get('genre', 'N/A')}")
        print(f"  Bewertung: {details.get('bewertung', 'N/A')}")
        print("-----------------------")

def film_hinzufuegen(): # GEÄNDERT: Mit Validierung
    print("\n--- Film hinzufügen ---")
    titel = input("Titel des Films: ")
    regisseur = input("Regisseur des Films: ")

    # Validierung für das Jahr
    while True:
        jahr_str = input("Erscheinungsjahr des Films: ")
        try:
            jahr = int(jahr_str)
            break
        except ValueError:
            print("Ungültige Eingabe. Das Jahr muss eine Zahl sein.")

    genre = input("Genre des Films: ")

    # Validierung für die Bewertung
    while True:
        bewertung_str = input("Bewertung (1-5 Sterne): ")
        try:
            bewertung = int(bewertung_str)
            if 1 <= bewertung <= 5:
                break
            else:
                print("Ungültige Bewertung. Bitte geben Sie eine Zahl zwischen 1 und 5 ein.")
        except ValueError:
            print("Ungültige Eingabe. Die Bewertung muss eine Zahl sein.")

    if titel in filme:
        print(f"Fehler: Film '{titel}' existiert bereits im Katalog.")
        return

    filme[titel] = {
        "regisseur": regisseur,
        "jahr": jahr,
        "genre": genre,
        "bewertung": bewertung
    }
    print(f"Film '{titel}' wurde hinzugefügt.")

def film_suchen():
    print("\n--- Film suchen ---")
    suchbegriff = input("Geben Sie einen Suchbegriff für den Titel ein: ").lower()
    gefundene_filme = {}

    for titel, details in filme.items():
        if suchbegriff in titel.lower():
            gefundene_filme[titel] = details

    if not gefundene_filme:
        print(f"Keine Filme gefunden, die '{suchbegriff}' im Titel enthalten.")
        return

    print(f"\n--- Gefundene Filme für '{suchbegriff}' ---")
    for titel, details in gefundene_filme.items():
        print(f"Titel: {titel}")
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print(f"  Genre: {details.get('genre', 'N/A')}")
        print(f"  Bewertung: {details.get('bewertung', 'N/A')}")
        print("-----------------------")

def film_loeschen():
    print("\n--- Film löschen ---")
    titel_zu_loeschen = input("Titel des zu löschenden Films: ")
    if titel_zu_loeschen in filme:
        del filme[titel_zu_loeschen]
        print(f"Film '{titel_zu_loeschen}' wurde aus dem Katalog entfernt.")
    else:
        print(f"Fehler: Film '{titel_zu_loeschen}' nicht im Katalog gefunden.")

def katalog_speichern():
    try:
        with open(DATEINAME, 'w', encoding='utf-8') as f:
            json.dump(filme, f, indent=4, ensure_ascii=False)
        print(f"Katalog erfolgreich in '{DATEINAME}' gespeichert.")
    except IOError as e:
        print(f"Fehler beim Speichern des Katalogs: {e}")

def katalog_laden():
    global filme
    try:
        with open(DATEINAME, 'r', encoding='utf-8') as f:
            filme = json.load(f)
        print(f"Katalog erfolgreich aus '{DATEINAME}' geladen.")
    except FileNotFoundError:
        print("Keine vorhandene Katalogdatei gefunden. Starte mit leerem Katalog.")
        filme = {}
    except json.JSONDecodeError as e:
        print(f"Fehler beim Laden des Katalogs (ungültiges JSON): {e}. Starte mit leerem Katalog.")
        filme = {}
    except Exception as e:
        print(f"Ein unerwarteter Fehler beim Laden ist aufgetreten: {e}. Starte mit leerem Katalog.")
        filme = {}

def zeige_menue():
    print("\n--- Filmkatalog Menü ---")
    print("1. Film hinzufügen")
    print("2. Filme anzeigen")
    print("3. Film suchen")
    print("4. Film löschen")
    print("5. Beenden")
    print("------------------------")

def main():
    katalog_laden()
    while True:
        zeige_menue()
        wahl = input("Ihre Wahl: ")

        if wahl == '1':
            film_hinzufuegen()
        elif wahl == '2':
            filme_anzeigen()
        elif wahl == '3':
            film_suchen()
        elif wahl == '4':
            film_loeschen()
        elif wahl == '5':
            katalog_speichern()
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
