import time
import json
from utilsl import UtilsL as ul
import re
class Log:

    @staticmethod
    def sout(obj):
        try:
            with open("sout.txt", "a+") as fa:
                fa.write(str(obj))
        except IOError:
            print("ERROR: IO")

    @staticmethod
    def saveGoodPrint(url, kwds):  # temp method TODO:// Substituir pelo save na DB
        timestamp = time.time()
        old_data = []
        with open("data/found.json", "r") as fb:
            read_data = json.load(fb)
            empty = ul.checkListEmpty(read_data)
            print("Read Data: " + str(read_data))
            if not empty:
                for elem in read_data:
                    old_data.append(elem)
        if type(kwds) == list:

            old_data.append([str(url), kwds])
        elif re.search("\\[", str(kwds)):
            old_data.append([str(url), eval(kwds)])
        else:
            old_data.append([str(url), str(kwds)])


        with open("data/found.json", "w") as fc:
            json.dump(old_data, fc)

