from bs4 import BeautifulSoup
import os
import requests

def create_directory(scraping):
    if not os.path.exists(scraping):
        os.mkdir(scraping)

def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data +'\n')

def read_data(path, data):
    with open(path,'rt') as file:
        current_line = 0
        for line in file:
            if current_line == file:
                break
            if line == "\n":
                continue
            else:
                current_line = current_line + 1
                print(line.replace("\n",""))

def does_file_exist(path):
    return os.path.exists(path)

def create_new_file(path):
    with open(path, 'w') as file:
        file.write("")   

def get_details(url):
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    divEntry = soup.find("article", {'class':'clearfix'})
    soup = BeautifulSoup(str(divEntry), "html.parser")
    paragraf = soup.find_all("p")
    write_to_file("berita kompas/artikel.doc", "isi berita: \n")
    for p in paragraf:
        write_to_file("berita kompas/artikel.doc", p.text)
    print("------------------------------------------------------------")
    write_to_file("berita kompas/artikel.doc", "=======================================================================")

# def main_scraper(url,directory):
# create_directory(directory) 