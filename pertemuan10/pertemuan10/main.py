from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://id.indeed.com/jobs?q=web+developer&l=jawa+timur&from=searchOnHP%2Cwhatautocomplete%2CwhatautocompleteSourceStandard&vjk=f918e7918fa63c19"
params = {
    'q': 'web+developer',
    'l': 'jawa+timur'
}
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
full_url = f"{url}q={params['q']}&l={params['l']}"
driver.get(full_url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all("div", class_='jobsearch-JobComponent-description css-jsfa0i eu4oa1w0')

print(data)