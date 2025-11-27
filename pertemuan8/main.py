from bs4 import BeautifulSoup
import requests
import os

url = "https://id.indeed.com/jobs?"
params = {
    'q': 'web+developer',
    'l': 'bali',
    'vjk': 'f53d052806d2f674'
}

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}

res = requests.get(url, headers=headers, params=params)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())

def get_total_pages():
    params = {
        'q': 'web+develope',
    	'l': 'bali',
    	'vjk': 'f53d052806d2f674'
    }
    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+', encoding='utf=8') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    get_total_pages()