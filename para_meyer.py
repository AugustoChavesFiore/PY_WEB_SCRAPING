import requests
from bs4 import BeautifulSoup
import re 
import os

    #ACA GUARDAMOS LAS IMG MEYER
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
      
        #ACA SACAMOS TODAS LAS URL DE LAS IMG MEYER
        img_url = []
        for img in results:
           if 'data-src' in img.attrs:
               img_url.append(img['data-src'])
        #ACA FILTAMOS LAS IMG CON LAS EXTENCIONES QUE QUEREMOS MEYER
        new_img_url = []
        for img in img_url:
            if re.search(r'\.jpg|\.png|\.webp', img) is not None:
                new_img_url.append(img)
        img_url = new_img_url
        
       #ACA GUARDAMOS LAS URL DE LAS IMG MEYER
        img_url = list(set(img_url))
        #ACA LLAMAMOS A LA FUNCION QUE GUARDA LAS IMG MEYER
        save_images(img_url)
    
    except Exception as e:
        print(f"Error: {e}")


get_images(url)

print("Images saved!")