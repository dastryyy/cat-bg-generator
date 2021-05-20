import os
import time
import requests
import ctypes
import urllib.request
import config
from unsplash.api import Api
from unsplash.auth import Auth

auth = Auth(config.client_id, config.client_secret, config.redirect_uri, code=config.code)
api = Api(auth)


def get_wallpaper():
    query = "kitten"
    photo = api.photo.random(query=query)
    photo_id = photo[0].id
    url = "https://api.unsplash.com/photos/%s/download?client_id=%s" % (photo_id, config.client_id)
    res = requests.get(url)
    if res.status_code == 200:
        photo = res.json()
        link = photo["url"]
        print(link)
        with open("img.jpg", "wb") as f:
            f.write(urllib.request.urlopen(link).read())
    else:
        print("unable to make request")


def set_wallpaper():
    get_wallpaper()
    path = os.getcwd() + "\\img.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

