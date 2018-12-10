from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_one():
    browser = init_browser()

    url = "https://www.bloomingdales.com/shop/product/marc-new-york-holden-down-parka-jacket?ID=3141068&RecProdZonePos=prodrec-1&LinkType=prodrec_pdpza&RecProdZoneDesc=RR-CMIO-RT-POC|RR-CMIO|prodrec_pdpza|RR/"

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #bloomingdales jacket site
    jacket_image = soup.find('li', class_='main-image')

    link = jacket_image.find('img', class_='main-image-img first-image')
    url = link['src']
    title = link['title']

    jackets = {"title": title, "img": url}

    return jackets