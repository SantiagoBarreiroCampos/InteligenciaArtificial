#Establecemos librerias
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time

#Hacemos uso de selenium, estableciendo la ubicacion de donde tenemos guardado el chromedriver
driver = webdriver.chrome('C:\Users\Usuario\Desktop\chromedriver.exe')
#Link de la página que queremos acceder
link_pagina = "https://www.ebay.com/"
#Producto al cual queremos hacer webscraping
busqueda = "samsung galaxy s10".replace("","+")
#url que genera el producto
driver.get(link_pagina + "/sch/i.html?_from=R40&_trksid=p2380057.m570.l1311&_nkw="+busqueda"&_sacat=0")

producto_titulo = []
producto_link = []
producto_subtitulo = []
producto_puntuaje = []
producto_precio = []

page = BeautifulSoup(driver.page_source,'html_parser')

#Extraemos de HTML la información que queremos guardar, en nuestro caso titulo, link, subtitulo, puntuaje y precio
for producto in page.findAll('li', attrs={'class': 's-item', 'data-view': True}):
    titulo = producto.find('h3', attrs={'class': 's-item__title'})
    if titulo:
        producto_titulo.append(titulo.text)
    else: producto_titulo.append('')

    link = producto.find('a', attrs={'class': 's-item_link'})
    if link:
        producto_link.append(link['href'])
    else: producto_link.append('')

    subtitulo = producto.find('div', attrs={'class': 's-item__subtitle'})
    if subtitulo:
        producto_subtitulo.append(subtitulo.text)
    else: producto_subtitulo.append('')

    puntuaje = producto.find('div', attrs={'class': ['b-starrating', 'x-star-rating']})
    if puntuaje:
        puntuaje.find('span', attrs={'class': 'clipped'})
        if puntuaje:
            producto_puntuaje.append(puntuaje.text)
        else: producto_puntuaje.append('')
    else: producto_puntuaje.append('')

    precio = producto.find('span', attrs={'class', 's-item__price'})
    if precio:
        producto_precio.append(precio.text)
    else:
        producto_precio.append('')

#Para poder verlo en modo tabla con el DataFrame a través de pandas
producto_lista = pd.DataFrame({'ID':producto_titulo,
                               'Titulo':producto_titulo,
                               'Subtitulo':producto_subtitulo,
                               'Puntuaje':producto_puntuaje,
                               'Precio':producto_precio,
                               'Link':producto_link
                               })

producto_lista.to_csv(r'C:\Users\Usuario\Desktop\Inteligencia Artificial\Web Scraping\webScraping.csv', index=None, header=True, encoding='utf-8-sig')
