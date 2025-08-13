# Day 22 of 30 days with python
import requests
from bs4 import BeautifulSoup
import json

# Fonction utilitaire pour enregistrer un fichier JSON
def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] {filename} sauvegardé.")


def scrape_bu_facts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "url": url,
        "title": soup.title.string.strip() if soup.title else "",
        "facts": []
    }

    # Chercher les listes <ul> et <ol> avec un titre
    for section in soup.find_all(["h2", "h3"]):
        heading = section.get_text(strip=True)
        nxt = section.find_next_sibling()
        items = []
        while nxt and nxt.name in ["ul", "ol"]:
            for li in nxt.find_all("li", recursive=False):
                items.append(li.get_text(strip=True))
            nxt = nxt.find_next_sibling()
        if items:
            data["facts"].append({"heading": heading, "items": items})

    return data

# (2) UCI datasets table -
def scrape_uci_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver le plus grand tableau sur la page
    tables = soup.find_all("table")
    main_table = max(tables, key=lambda t: len(t.find_all("tr")))

    # Extraire l'en-tête
    headers = [th.get_text(strip=True) for th in main_table.find_all("th")]

    rows_data = []
    for row in main_table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all("td")]
        if cells:
            row_dict = {headers[i] if i < len(headers) else f"col{i+1}": cells[i] for i in range(len(cells))}
            rows_data.append(row_dict)

    return {"url": url, "headers": headers, "rows": rows_data}

#  (3) Wikipedia US Presidents
def scrape_us_presidents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Chercher la table des présidents
    tables = soup.find_all("table", {"class": "wikitable"})
    presidents_table = None
    for table in tables:
        if "President" in table.get_text():
            presidents_table = table
            break

    headers = [th.get_text(strip=True) for th in presidents_table.find_all("th")]

    rows_data = []
    for row in presidents_table.find_all("tr")[1:]:
        cells = [td.get_text(" ", strip=True) for td in row.find_all(["td", "th"])]
        if cells:
            row_dict = {headers[i] if i < len(headers) else f"col{i+1}": cells[i] for i in range(len(cells))}
            rows_data.append(row_dict)

    return {"url": url, "headers": headers, "rows": rows_data}

if __name__ == "__main__":
    bu_url = "http://www.bu.edu/president/boston-university-facts-stats/"
    uci_url = "https://archive.ics.uci.edu/ml/datasets.php"
    wiki_url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

    bu_data = scrape_bu_facts(bu_url)
    save_json(bu_data, "bu_facts_stats.json")

    #uci_data = scrape_uci_table(uci_url)
    #save_json(uci_data, "uci_datasets.json")

    presidents_data = scrape_us_presidents(wiki_url)
    save_json(presidents_data, "us_presidents.json")

