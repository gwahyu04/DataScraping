# import os
# from bs4 import BeautifulSoup
# import requests

# def create_directory(directory):
#     if not os.path.exists(directory):
#         os.mkdir(directory)

# def write_to_file(path, data):
#     with open(path,'a') as file:
#         file.write(data + '\n')

# def read_data(path, limit):
#     with open(path,'rt') as file:
#         count = 0
#         for line in file:
#             if count == limit:
#                 break
#             if line == "\n":
#                 continue
#             else:
#                 count += 1
#                 print(line.replace("\n",""))
                

# def does_file_exist(path):
#     return os.path.isfile(path)

# def remove_file(path):
#     if does_file_exist(path):
#         os.remove(path)
#     else:
#         print("file tidak ada")

# def create_new_file(path):
#     with open(path, 'w') as file:
#         file.write("")

# def get_details(url):
#     source_code = requests.get(url)
#     source_text = source_code.text
#     soup = BeautifulSoup(source_text, "html.parser")
#     diventry = soup.find("article", {"class" : "clearfix"})
#     soup = BeautifulSoup(str(diventry), "html.parser")
#     paragraf = soup.find_all("p")
#     write_to_file("berita kompas/artikel.doc", "isi berita : \n")
    
#     for p in paragraf:
#         write_to_file("berita kompas/artikel.doc", p.text)
#     print(' -------------------------------------------------------------------------- ')
#     write_to_file("berita kompas/artikel.doc", "--------------------------------")

import os


def create_directory(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' berhasil dibuat")


def does_file_exist(file_path):
    return os.path.exists(file_path)


def write_to_file(file_path, content):
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def append_to_file(file_path, content):
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)


def read_data(path, lines=None):
    if not os.path.exists(path):
        print(f"File '{path}' tidak ditemukan.")
        return

    with open(path, "r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            if lines is not None and index >= lines:
                break
            print(line.rstrip())


if __name__ == "_main_":
    read_data("Hasil/hasil_scraping.txt", 6)