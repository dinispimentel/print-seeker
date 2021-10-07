from new.Print import Print
from new.log import Log
from new.utilsl import UtilsL as ul
import time


class tT:

    def __init__(self):
        self._running = False
        self.actual_url = ""

    def startIfShould(self, instance):
        """
        :param instance É a função que vai retornar a url para esta thread usar na sequência.
        """
        self._running = True

        print("Iniciando processo")
        while self._running:
            time.sleep(1)

            print("lm Thread Hash: " + str(hex(id(instance))))


            self.actual_url = instance.retrieveLinkForWork()
            # print("Actual url" + str(self.actual_url))
            sS = Print(self.actual_url)
            sS.downloadImage()
            sS.getKwds()

            if not ul.checkListEmpty(sS.kwds):
                print("PRINT: " + self.actual_url + "\n" + "KWDS: " + str(sS.kwds))
                sS.saveImage()
                # TODO:// Adicionar à DB para website ou Hooker no discord [Se hooker, colocar um bot com login para cada user]

    def askToStop(self):

        self._running = False
