import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")
soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})

titles = populer_area.findAll(attrs={'class': 'media__title'})
images = populer_area.findAll(attrs={'class': 'media__image'})
dates  = populer_area.findAll(attrs={'class': 'media__date'})

for title, image, date in zip(titles, images, dates):
    judul = title.text.strip()

    img = image.find('img')
    gambar = img['src'] if img else '-'

    waktu = date.text.strip()

    print("Judul :", judul)
    print("Waktu :", waktu)
    print("Gambar:", gambar)
    print("-" * 40)
 #pake array jika ingin mengambil salah satu element saja

#texts = populer_area.findAll(attrs={'class': 'media__title'})
#images = populer_area.findAll(attrs={'class': 'media__image'})

#for image in images:
#    print(image.find('a').find('img'))

