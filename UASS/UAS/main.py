import requests
from bs4 import BeautifulSoup
import re

def get_minutes(text):
    digits = re.findall(r'\d+', text)
    val = int(digits[0]) if digits else 999
    if 'jam' in text: val *= 60
    return val

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")
soup = BeautifulSoup(html_doc.text, 'html.parser')
titles = soup.find(attrs={'class': 'grid-row list-content'}).findAll(attrs={'class': 'media__title'})
dates = soup.find(attrs={'class': 'grid-row list-content'}).findAll(attrs={'class': 'media__date'})

# Gabungkan dan urutkan
news_list = []
for t, d in zip(titles, dates):
    news_list.append({'j': t.text.strip(), 'w': d.text.strip(), 'm': get_minutes(d.text.strip())})

news_sorted = sorted(news_list, key=lambda x: x['m'])

print(f"{'WAKTU':<15} | {'JUDUL'}")
print("-" * 60)
for n in news_sorted:
    print(f"{n['w']:<15} | {n['j'][:50]}...")