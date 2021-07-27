#  Ejemplo de web scraping con python

from bs4 import BeautifulSoup
import requests

url = requests.get("https://camara-arequipa.org.pe/dirempresarial/")

status_code = url.status_code
if status_code == 200:
    # print(url)
    html = BeautifulSoup(url.text,"html.parser")
    # print(html)
    
    empresas = html.find_all('div',{'class':'card-body'})
    # print(empresas)
    
    for empresa in empresas:
        nombre = empresa.find('h5',{'class':'card-title'})
        print(nombre)

else:
    print("error nro: " + str(status_code))
