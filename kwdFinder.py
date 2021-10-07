import pytesseract
import re
import json
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

class kF:

    ft = []
    bft = []
    with open('config/keywords.json') as f:
        ft = json.load(f)
    with open('config/blacklist_keywords.json') as bf:
        bft = json.load(bf)

    def __init__(self, image):
        self.image = image
        self.text = ""
        self.kwds = []


    def _filterStringKwds(self):
        for fil in kF.ft:
            if re.search(str(fil), self.text) is not None:
                self.kwds.append(fil)

        for bfil in kF.bft:
            if re.search(str(bfil), self.text) is not None:
                self.kwds = []
                return False

    def findKeywords(self):
        try:
            self.text = pytesseract.image_to_string(self.image)
            res = self._filterStringKwds()
            if res is False:
                print("Blacklist!")
        except TypeError:
            pass
        return self.kwds
