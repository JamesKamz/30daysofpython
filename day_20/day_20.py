#Day 20 of 30 days with python
import requests, re, statistics
from collections import Counter
from bs4 import BeautifulSoup


romeo_and_juliet ='http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet).txt.lower()
words = re.findall(r'\b\w+\b', response)
top10 = Counter(words).most_common(10)
print("Top 10 mots :", top10)


cats = requests.get('https://api.thecatapi.com/v1/breeds').json()
weights = []
lifespans = []
country_counter = Counter()

for c in cats:
    w = c.get('weight', {}).get('metric', '')
    ls = c.get('life_span', '')
    origin = c.get('country_codes') or c.get('origin') or 'Unknown'
    country_counter[origin] += 1
    for data, coll in [(w, weights), (ls, lifespans)]:
        m = re.findall(r'\d+\.?\d*', data)
        if len(m) >= 2:
            low, high = map(float, m[:2])
            coll.append((low + high) / 2)

def stats(name, arr):
    if arr:
        print(f"{name}: min={min(arr)}, max={max(arr)}, mean={statistics.mean(arr):.2f}, median={statistics.median(arr):.2f}, stdev={statistics.stdev(arr):.2f}")
    else:
        print(f"{name}: no data")

stats("Weight (kg)", weights)
stats("Lifespan (years)", lifespans)
print("Count by country_codes/origin:", country_counter.most_common(10))

countries = requests.get('https://restcountries.com/v3.1/all').json()

largest = sorted(countries, key=lambda x: x.get('area', 0), reverse=True)[:10]
print("10 plus grands pays:", [c.get('name', {}).get('common') for c in largest])

lang_counter = Counter()
for c in countries:
    langs = c.get('languages') or {}
    for lang in langs.values():
        lang_counter[lang] += 1

print("10 langues les plus parlées:", lang_counter.most_common(10))
print("Total de langues uniques:", len(lang_counter))

# 4. UCI datasets
uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
html = requests.get(uci_url).text
soup = BeautifulSoup(html, 'html.parser')
# Exemple: récupérer tous les noms de datasets
for link in soup.select('table[border=1] tbody tr td a'):
    print(link.text)