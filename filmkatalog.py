# Hauptcode für Filmkatalog
filme = {} # Ein Dictionary zum Speichern der Filme. Schlüssel: Filmtitel, Wert: Dictionary mit Details

def filme_anzeigen():
    # Überprüfe, ob das 'filme'-Dictionary leer ist
    if not filme:
        print("Der Katalog ist leer.")
        return # Beende die Funktion hier, wenn keine Filme vorhanden sind

    print("\n--- Dein Filmkatalog ---")
    # Iteriere über alle Filme im Dictionary
    for titel, details in filme.items():
        print(f"Titel: {titel}")
        # Verwende .get(), um 'N/A' anzuzeigen, falls ein Detail fehlt
        print(f"  Regisseur: {details.get('regisseur', 'N/A')}")
        print(f"  Jahr: {details.get('jahr', 'N/A')}")
        print("-----------------------")

# Test der Funktion (diese Zeile wird später durch ein Menü ersetzt)
filme_anzeigen()
