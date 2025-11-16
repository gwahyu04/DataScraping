from bs4 import BeautifulSoup # untuk parsing(mengurai) HTML dan XML
import os # untuk berinteraksi dg sistem operasi
import scraping # import file scraping
import requests # untuk membuat permintaan HTTP ke URL yang diberikan dan mendapatkan konten HTML dari halaman web.
# soup = BeautifulSoup('<html><body><div class="class1">''</div><div class="class2"></div><div class="class3"></div></body></html>')
# soup.findAll(True, {"class":["class1", "class2"]}) #mencari tag apapun (ga peduli div,p selama classnya sama)
# def main_scraper(url,directory,file): # menerima argumen url, nama folder tmpat hasilny disimpen, file text buat nyimpen
#     scraping.create_directory(directory) # memanggil dari file scraping apkh file sudah ada
#     source_code = requests.get(url) # mengirim permintaan untuk mengambil url , source code itu variabel
#     source_text = source_code.text # mengambil HTML yang berupa string/text
#     soup = BeautifulSoup(source_text,"html.parser") # mengambil text html & menggunakan parser untuk mengubah jadi strukur yg dpt di navigasi
#     # articles = soup.find_all("h3",{'class':'article__title article__title--medium'})
#     # articles2 = soup.find_all(True,{'class':['article__box','article__title']})
#     articles = soup.find_all(True,{'class':['row article__wrap__grid--flex col-offset-fluid mt2', 'article__title']})
    # menampilkan semua tag apa saja

    # for article in articles:
    #     print("URL : " + article.a.get("href"))
    #     print("judul : " + article.text)
    #     print()
    # for article2 in articles2:
    #     print("URL2 : " + article2.a.get("href"))
    #     print("judul2 : " + article2.text)
    #     print()
    # for article in articles[:3]:
    #     print("URL : " + article.a.get("href")) 
    #     print("judul : " + article.a.text)
    #     file_path = os.path.join(directory, file)
    #     scraping.write_to_file(file_path, "URL: " + article.a.get("href"))
    #     scraping.write_to_file(file_path, "Judul: " + article.a.text + "\n")
    #     scraping.get_details(article.a.get("href"))
    #     print(article_format)

scraping.create_directory("berita kompas")

def main_scraper(url, directory):
    scraping.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find_all(True, {'class':'clearfix'})

    for article in articles:
        article_format = "URL: " + article.a.get("href") + "\n"

        if scraping.does_file_exist(directory + "/artikel.txt") is False:
            scraping.create_new_file(directory + "/artikel.txt")

        scraping.write_to_file(directory + "/artikel.txt", article_format)
        scraping.get_details(article.a.get("href"))
        print(article_format)


# def read_data(path):
#     with open(path,'rt') as file:
#         for line in file:
#             print(line)

# def write_to_file(path,data):
#     with open(path,'a') as file:
#         file.write(data +'\n')

# write_to_file("hasil/hasil.txt","Hasil")
# read_data("hasil/hasil.txt")
main_scraper("https://tekno.kompas.com/read/2025/10/29/17150097/melihat-oppo-find-x9-dan-x9-pro-dari-dekat-hp-flagship-yang-segera-rilis-di","Hasil5")