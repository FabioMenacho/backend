#  Ejemplo de web scraping con python

from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")

status_code = url.status_code
if status_code == 200:
    # print(url)
    html = BeautifulSoup(url.text,"html.parser")
    # print(html)
    
    empresas = html.find_all('tr',{'class':'rgRow'})
    # print(empresas)
    
    for empresa in empresas:
        moneda = empresa.find('td',{'class':'APLI_fila3'})
        tipocambio = empresa.find('td',{'class':'APLI_fila2'})
        print(str(moneda) + " - " + str(tipocambio))

else:
    print("error nro: " + str(status_code))
