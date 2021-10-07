from new.kwdFinder import kF
from new.lightGet import lG
from new.log import Log
from new.utilsl import UtilsL as ul


class Print:


    def __init__(self, url):

        self.url = url
        self.image = None
        self.kwds = []



    def downloadImage(self):
        # print("Received URL: " + self.url)
        lg = lG(self.url)
        self.image = lg.getImage()


    def getKwds(self):
        kf = kF(self.image)
        self.kwds = kf.findKeywords()

    def saveImage(self):
        if not ul.checkListEmpty(self.kwds):
            Log.saveGoodPrint(self.url, self.kwds)



