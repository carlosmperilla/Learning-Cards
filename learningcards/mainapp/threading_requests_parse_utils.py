import requests

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs 
from random import randint

def get_img_google(obj, url_img):
    g_req = requests.get(url_img)
    g_parser = bs(g_req.content, 'html.parser')
    obj.img = g_parser.findAll("img")[randint(1,20)]["src"]
    return obj

def threading_get_imgs(objects, attr_name):
    with ThreadPoolExecutor() as executor:
            for obj in objects:
                word_to_search = obj.__getattribute__(attr_name)
                url_name = requests.utils.quote(word_to_search)
                url_img = f"https://www.google.com/search?q={url_name}&tbm=isch&tbs=isz:l"
                executor.submit(get_img_google, obj=obj, url_img=url_img)