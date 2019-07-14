from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def getHTML(link):
    
    uClient = uReq(link)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    
    return page_soup
    