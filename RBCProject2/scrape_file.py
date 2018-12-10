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

    link = jacket_image.find('img', class_='main-image-img')
    url = link['src']
    title = link['title']

    jackets = { "title": title, "image": url}

    return jackets

def scrape_two():
    browser = init_browser()

    url = "https://www.bloomingdales.com/shop/product/frame-lhomme-slim-fit-jeans-in-blue-bay?ID=3147186&CategoryID=10172#fn=ppp%3Dundefined%26sp%3DNULL%26rId%3DNULL%26spc%3D554%26spp%3D1%26pn%3D1%7C6%7C1%7C554%26rsid%3Dundefined%26smp%3DmatchNone/"

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #bloomingdales jeans
    jeans_image = soup.find("li", class_="main-image")

    link = jeans_image.find('img', class_= "main-image-img")
    url = link["src"]
    title = link["title"]

    jeans = {"title": title, "image": url}

    return jeans

def scrape_three():
    browser = init_browser()

    url = "https://www.bloomingdales.com/shop/product/john-varvatos-star-usa-mens-zander-suede-chukka-boots?ID=3107596&CategoryID=1000046#fn=ppp%3Dundefined%26sp%3DNULL%26rId%3DNULL%26spc%3D159%26spp%3D4%26pn%3D1%7C2%7C4%7C159%26rsid%3Dundefined%26smp%3DmatchNone/"

    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #bloomingdales shoes
    shoes_image = soup.find("li", class_="main-image")

    link = shoes_image.find('img', class_= "main-image-img")
    url = link["src"]
    title = link["title"]

    shoes = {"title": title, "image": url}

    return shoes