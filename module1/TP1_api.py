import requests

# URL de l'API Chronicling America
url = "https://chroniclingamerica.loc.gov/search/pages/results/"

# Boucle pour les années entre 1900 et 1914
for year in range(1900, 1915):
    # Paramètres de la requête pour chaque année
    params = {
        "andtext": "vampire OR vampires",  # Rechercher les termes "vampire" ou "vampires"
        "date1": f"{year}1030",  # Début de la plage de date (30 octobre de l'année)
        "date2": f"{year}1101",  # Fin de la plage de date (1er novembre de l'année)
        "format": "json",  # Format de la réponse
        "rows": 10  # Limite de résultats
    }

    # Effectuer la requête GET
    response = requests.get(url, params=params)

    # Vérifier si la requête est réussie
    if response.status_code == 200:
        # Extraire les données en format JSON
        data = response.json()
        
        # Vérifier s'il y a des résultats
        if 'items' in data:
            print(f"Résultats pour l'année {year}:")
            for item in data['items']:
                print(f"Title: {item['title']}")
                print(f"Date: {item['date']}")
                print(f"Page: {item['page']}")
                print(f"LCCN: {item['lccn']}")
                print(f"URL de l'édition numérisée: {item['url']}\n")
        else:
            print(f"Aucun résultat trouvé pour l'année {year}.")
    else:
        print(f"Échec de la requête pour l'année {year} : {response.status_code}")
