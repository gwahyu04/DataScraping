# from bs4 import BeautifulSoup
# import fungsi 
# import requests

# def main_scraper(url):
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")
#     articles = soup.find_all("article", {'class' : 'container clearfix'})

#     print(articles)

# main_scraper("https://news.kompas.com/?source=navbar")


# from selenium import webdriver
# from bs4 import BeautifulSoup

# url = "https://tekno.kompas.com/gadget"

# driver = webdriver.Chrome()
# driver.get(url)                   

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# data = soup.find_all("div", class_="latest--news mt2 clearfix")  

# print(data)

# driver.quit()

# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver

# def main_scraper(url):
#     source_code = requests.get(url)
#     source_text = source_code.text
#     url = "https://tekno.kompas.com/gadget"
#     driver = webdriver.Chrome()
#     driver.get(url)
#     soup = BeautifulSoup(source_text, 'html.parser')
#     articles = soup.find_all("article", {'class':'latest--news mt2 clearfix'})
#     print(articles)
#     driver.quit()

# main_scraper("https://tekno.kompas.com/gadget")

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import fungsi
# import requests
# import os

# def main_scraper(url):
#     source_code = requests.get(url)
#     headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
#     driver = webdriver.Chrome()
#     driver.set_page_load_timeout(5000)
#     full_url = f"{url}"
#     driver.get(full_url)
#     html = driver.page_source
#     soup = BeautifulSoup('html', 'html.parser')
#     hasil = soup.find_all("div", class_='latest--news mt2 clearfix')
    
#     for i in range(len(hasil)):
#         Card = hasil[i].find("div", {'class':'article__list clearfix'})
#         Judul = hasil[i].find("a", {'class':'article__link'})
#         if Card and Judul:
#             print("Card : " + Card.text)
#             print("Judul : " + Judul.text)
#             print("=====================================")

#     fungsi.create_directory('hasil')
#     file_path = os.path.join('hasil', 'kompasparser.txt')
#     fungsi.write_to_file(file_path, 'html')
#     print(html)

# main_scraper("https://tekno.kompas.com/gadget")


# from selenium import webdriver
# from bs4 import BeautifulSoup
# import fungsi
# import os
# import time

# def main_scraper(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
#                       '(KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
#     }

#     driver = webdriver.Chrome()
#     driver.get(url)
#     time.sleep(3)

#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')

#     # AMBIL SEMUA ITEM BERITA
#     items = soup.find_all("div", class_="article__list")

#     print("Total artikel ditemukan:", len(items))

#     for item in items:
#         # Judul
#         judul_tag = item.find("a", class_="article__link")
#         judul = judul_tag.text.strip() if judul_tag else "-"

#         # Isi Card (judul + kategori + tanggal)
#         card = item.get_text(strip=True)

#         print("Card :", card)
#         print("Judul :", judul)
#         print("=====================================")

#     # SIMPAN HTML KE FILE
#     fungsi.create_directory('hasil')
#     file_path = os.path.join('hasil', 'kompasparser.txt')
#     fungsi.write_to_file(file_path, html)

#     driver.quit()


# main_scraper("https://tekno.kompas.com/gadget")

from selenium import webdriver
from bs4 import BeautifulSoup
import fungsi
import os
import time

def main_scraper(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # CARI artikel, bukan div
    items = soup.find_all("article", class_="latest--news mt2 clearfix")
    print("Total artikel ditemukan:", len(items))

    for item in items:

        # blok utama card
        card = item.find("div", class_="article__list")

        # Judul
        judul_tag = item.find("h3", class_="article__title")
        judul = judul_tag.text.strip() if judul_tag else "-"

        # Kategori
        kategori_tag = item.find("div", class_="article__subtitle")
        kategori = kategori_tag.text.strip() if kategori_tag else "-"

        # Tanggal
        tanggal_tag = item.find("div", class_="article__date")
        tanggal = tanggal_tag.text.strip() if tanggal_tag else "-"

        # Cuplikan isi berita
        lead_tag = item.find("p", class_="article__lead")
        lead = lead_tag.text.strip() if lead_tag else "-"

        print("Judul   :", judul)
        print("Kategori:", kategori)
        print("Tanggal :", tanggal)
        print("Isi     :", lead)
        print("=====================================")

    # simpan html mentah
    fungsi.create_directory('hasil')
    file_path = os.path.join('hasil', 'kompasparser.txt')
    fungsi.write_to_file(file_path, html)

    driver.quit()


main_scraper("https://tekno.kompas.com/gadget")


