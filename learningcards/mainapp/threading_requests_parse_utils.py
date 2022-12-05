from random import randint
import requests
from bs4 import BeautifulSoup as bs 
from concurrent.futures import ThreadPoolExecutor

from typing import Union, List
from django.db.models import QuerySet
from kit.models import Kit
from card.models import Card

def get_img_google(obj : Union[Kit, Card], url_img : str) -> Union[Kit, Card]:
    """
        Make a request to the url containing the image and assign the url to the instance.
    """
    g_req = requests.get(url_img)
    g_parser = bs(g_req.content, 'html.parser')
    obj.img = g_parser.findAll("img")[randint(1,20)]["src"]
    return obj

def buil_url(obj : Union[Kit, Card], attr_name : str) -> str:
    """
        Build the url to make the request.
    """
    word_to_search = obj.__getattribute__(attr_name)
    url_name = requests.utils.quote(word_to_search)
    url_img = f"https://www.google.com/search?q={url_name}&tbm=isch&tbs=isz:l"
    return url_img

def threading_get_imgs(objects : Union[QuerySet, List[Card], List[Kit]], attr_name : str) -> None:
    """
        Performs requests via a pool of threads.
    """
    with ThreadPoolExecutor() as executor:
            for obj in objects:
                url_img = buil_url(obj, attr_name)
                executor.submit(get_img_google, obj=obj, url_img=url_img)