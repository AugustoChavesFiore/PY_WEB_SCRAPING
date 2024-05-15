import requests
from bs4 import BeautifulSoup
import re 
import json

url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'
try:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    result_ancords = soup.find_all('a')
except Exception as e:
    print(f"Error: {e}")

formated_result = {}

try:
    for a in result_ancords:
        url = a['href']
        exp= re.compile(r'^https://www.mercadolibre.com.ar/')
        if exp.match(url):
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"Error: {response.status_code}")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            h1 = soup.find_all('h1')
            p = soup.find_all('p')
            if h1 and p:
                formated_result[url] = [str(h1), str(p)]
            else:
                formated_result[url] = []
except Exception as e:
    print(f"Error: {e}")

json_result = json.dumps(formated_result)
print(json_result)