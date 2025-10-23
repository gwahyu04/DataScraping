import requests
from bs4 import BeautifulSoup  # ✅ perbaikan: tambahkan import BeautifulSoup
import fungsi  # pastikan ada file fungsi.py dengan fungsi create_directory()

# INFO REQUEST
result = requests.get("https://www.detik.com/")
print(result)
print(result.encoding)
print(result.status_code)
print(result.elapsed)
print(result.url)
print(result.history)
print(result.headers["Content-Type"])

# LOGIC
def main_scraper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")  # ✅ perbaikan ejaan: BeautifulSoup (bukan BeautifullSoup)
    print(soup.find_all("div", {"class": "media media--image-radius block-link"}))

# panggil fungsi
main_scraper("https://www.detik.com/", "Hasil")
