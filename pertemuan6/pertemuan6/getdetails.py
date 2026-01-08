# from bs4 import BeautifulSoup
# import fungsi
# import requests

# def main_scraper(url, directory):
#     fungsi.create_directory(directory)
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")
#     articles = soup.find_all(True, {"class" : "col-bs9-3"})

#     for article in articles:
#         article_format = "URL : " + article.a.get("href") + "\n"
        
#         if fungsi.does_file_exist(directory + "/artikel.txt") is False:
#             fungsi.create_new_file(directory + "/artikel.txt")
        
#         fungsi.write_to_file(directory + "/artikel.txt", article_format)
#         fungsi.get_details(article.a.get("href"))
#         print(article_format)

# fungsi.remove_file("hasil/articles.txt")
# main_scraper("https://tekno.kompas.com/read/2025/10/29/18580047/menggenggam-realme-15t-5g-hp-tipis-baterai-besar-yang-ringan-di-tangan","articles.txt")



# from bs4 import BeautifulSoup
# import fungsi
# import requests
# import os

# def main_scraper(url, directory, filename):
#     fungsi.create_directory(directory)
#     print("Folder sudah dibuat:", directory)

#     filepath = f"{directory}/{filename}"
#     print("File output:", filepath)

#     source_code = requests.get(url)
#     soup = BeautifulSoup(source_code.text, "html.parser")

#     articles = soup.find_all(True, {"class": "article__list__title"})
#     print("Jumlah artikel ditemukan:", len(articles))

#     for article in articles:
#         link_tag = article.find_all("a")
#         if not link_tag:
#             continue

#         article_format = "URL : " + link_tag.get("href") + "\n"

#         if not fungsi.does_file_exist(filepath):
#             fungsi.create_new_file(filepath)

#         fungsi.write_to_file(filepath, article_format)
#         print("Tulis:", article_format)

#     print("Selesai scraping.")


# main_scraper(
#     "https://tekno.kompas.com/read/2025/10/29/17150097/melihat-oppo-find-x9-dan-x9-pro-dari-dekat-hp-flagship-yang-segera-rilis-di",
#     "hasil",
#     "articles.doc"
# )


import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from fungsi import append_to_file, create_directory, does_file_exist, write_to_file


USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) Chrome/127 Safari/537"


def ambil_halaman(url):
    headers = {"User-Agent": USER_AGENT}
    respons = requests.get(url, timeout=30, headers=headers)
    respons.raise_for_status()
    return BeautifulSoup(respons.text, "html.parser")


def simpan_link_berita(soup, base_url, folder, hasil_file):
    daftar_link = soup.select("h3.article__title a")
    if not daftar_link:
        print("Tidak menemukan daftar artikel.")
        return []

    url_unik = []
    for link in daftar_link:
        href = link.get("href")
        if not href:
            continue

        url_artikel = urljoin(base_url, href)
        if url_artikel in url_unik:
            continue

        url_unik.append(url_artikel)
        judul = link.get_text(strip=True)

        teks = f"Judul: {judul}\nURL: {url_artikel}\n\n"
        if does_file_exist(hasil_file):
            append_to_file(hasil_file, teks)
        else:
            write_to_file(hasil_file, teks)

    if url_unik:
        print(f"Jumlah artikel yang disimpan: {len(url_unik)}")
    return url_unik


def simpan_isi_artikel(url, folder_detail):
    soup = ambil_halaman(url)
    konten = soup.select_one("div.read__content")
    if konten is None:
        print(f"Konten artikel tidak ditemukan: {url}")
        return

    paragraf = []
    for p in konten.find_all("p"):
        teks = p.get_text(strip=True)
        if teks:
            paragraf.append(teks)

    if not paragraf:
        print(f"Tidak ada paragraf pada artikel: {url}")
        return

    detail_file = os.path.join(folder_detail, "artikel.doc")
    append_to_file(detail_file, f"URL: {url}\nParagraf:\n")
    for teks in paragraf:
        append_to_file(detail_file, teks + "\n")
    append_to_file(detail_file, "=" * 100 + "\n\n")


def main_scraper(url, folder):
    create_directory(folder)
    hasil_file = os.path.join(folder, "hasil_scraping.doc")

    soup = ambil_halaman(url)
    daftar_url = simpan_link_berita(soup, url, folder, hasil_file)

    if not daftar_url:
        return

    folder_detail = os.path.join(folder, "detail")
    create_directory(folder_detail)

    for url_artikel in daftar_url:
        simpan_isi_artikel(url_artikel, folder_detail)

    print(f"Hasil scraping tersimpan di {hasil_file}")


main_scraper("https://tekno.kompas.com/", "Hasil")

