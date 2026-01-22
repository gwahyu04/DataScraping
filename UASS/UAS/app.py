from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def konversi_menit(waktu_str):
    """Mengonversi teks waktu detikcom ke angka menit untuk sorting"""
    angka = re.findall(r'\d+', waktu_str)
    angka = int(angka[0]) if angka else 999
    
    if 'detik' in waktu_str:
        return angka / 60
    elif 'menit' in waktu_str:
        return angka
    elif 'jam' in waktu_str:
        return angka * 60
    elif 'hari' in waktu_str:
        return angka * 1440
    return 9999

def cek_kategori(judul):
    # Kata kunci Alam/Lingkungan (Warna Merah)
    kata_alam = [
        'hujan', 'banjir', 'gempa', 'cuaca', 'gunung', 'alam', 'lingkungan', 
        'hutan', 'sungai', 'laut', 'angin', 'longsor', 'erupsi', 'bmkg', 'mendung'
    ]
    judul_lower = judul.lower()
    return 'merah' if any(kata in judul_lower for kata in kata_alam) else 'hijau'

def scrape_berita():
    url = "https://www.detik.com/jatim/berita/indeks"
    try:
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text, "html.parser")
        list_area = soup.find(attrs={'class': 'grid-row list-content'})

        titles = list_area.findAll(attrs={'class': 'media__title'})
        images = list_area.findAll(attrs={'class': 'media__image'})
        dates = list_area.findAll(attrs={'class': 'media__date'})

        data = []
        for title, image, date in zip(titles, images, dates):
            judul_text = title.text.strip()
            waktu_text = date.text.strip()
            img_tag = image.find('img')
            
            data.append({
                'judul': judul_text,
                'gambar': img_tag['src'] if img_tag else "",
                'tanggal': waktu_text,
                'warna': cek_kategori(judul_text),
                'menit_total': konversi_menit(waktu_text) # Digunakan untuk sorting
            })
        
        # Sorting berdasarkan waktu (paling baru / menit terkecil di atas)
        return sorted(data, key=lambda x: x['menit_total'])

    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route("/")
def index():
    berita = scrape_berita()
    return render_template("index.html", berita=berita)

if __name__ == "__main__":
    app.run(debug=True)