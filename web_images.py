import requests
from bs4 import BeautifulSoup
import re 
import os

    
def save_images(images):
    if not os.path.exists('images'):
        os.makedirs('images')
    for i, img in enumerate(images):
        response = requests.get(img)
        if response.status_code == 200:
            with open(f'images/img_{i}.jpg', 'wb') as f:
                f.write(response.content)
        else:
            print(f"Error: {response.status_code}")
            break
    print(f"{len(images)} images saved!")
        
url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'

def get_images(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('img', class_="dynamic-carousel__img")
        img_url= [img['data-src'] for img in results if 'data-src' in img.attrs]
        img_url = [img for img in img_url if re.search(r'\.jpg|\.png', img) is not None]
        img_url = list(set(img_url))
        save_images(img_url)
    
    except Exception as e:
        print(f"Error: {e}")


get_images(url)

print("Images saved!")