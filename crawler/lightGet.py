import cfscrape
import requests
import io
from bs4 import BeautifulSoup as bs
import re


from PIL import Image

# Class attributes are defined outside of constructor


class lG:

    def __init__(self, url):
        # Instance attributes are defined in the constructor
        self.url = url
        self.image = None


    def getImage(self):
        # print("lG instance url: " + self.url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-PT,pt;q=0.8,en;q=0.5,en-US;q=0.3',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
        }

        response = requests.get(self.url, headers=headers)
        # print("Response.content: " + str(response.content))
        if int(response.status_code) != 200:
            return -1

        soup = bs(response.content, 'html.parser')
        imgs = soup.select("img.no-click.screenshot-image")

        src = ""
        for img in imgs:

            _src = img.attrs['src']
            # print("_src: " + _src)
            if re.search("(\\.gif|\\.jpeg|/image/|\\.png|\\.jfif|\\.jpg)", _src):
                # print("AQUI!")
                src = _src
                # print("\n 1#: SRC/_SRC: " + src + " | " +_src)
        # print("\n 2#: SRC: " + src )

        img_response = requests.get(src, headers=headers)
        image_bytes = io.BytesIO(img_response.content)

        return Image.open(image_bytes)

