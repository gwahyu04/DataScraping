from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
# Menambahkan import datetime jika Anda ingin menggunakan waktu sistem
from datetime import datetime 

app = Flask(__name__)

def scrape_berita():
    url = "https://www.detik.com/jatim/berita/indeks"
    try:
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text, "html.parser")

        populer_area = soup.find(attrs={'class': 'grid-row list-content'})

        # Mengambil elemen judul, gambar, dan tanggal
        titles = populer_area.findAll(attrs={'class': 'media__title'})
        images = populer_area.findAll(attrs={'class': 'media__image'})
        dates = populer_area.findAll(attrs={'class': 'media__date'})

        data = []

        for title, image, date in zip(titles, images, dates):
            judul = title.text.strip()
            
            # Mencari tag img di dalam pembungkusnya
            img_tag = image.find('img')
            img_url = img_tag['src'] if img_tag else ""
            
            # Mengambil teks tanggal asli dari website
            waktu_asli = date.text.strip()

            data.append({
                'judul': judul,
                'gambar': img_url,
                'tanggal': waktu_asli # Kunci diubah jadi 'tanggal' agar sesuai index.html
            })

        return data
    except Exception as e:
        print(f"Terjadi kesalahan saat scraping: {e}")
        return []

@app.route("/")
def index():
    berita = scrape_berita()
    return render_template("index.html", berita=berita)

if __name__ == "__main__":
    app.run(debug=True)