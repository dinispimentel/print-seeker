import json
from new.Conf import Conf




class lM:

    aToX = {}
    xToA = {}
    config = Conf.config
    num_of_digits = config.get("code_digit_num")
    max_digit_range = config.get("digit_max_range")
    url_prefix = config.get("url_form")

    with open("refs/alphaToX.json", "r") as f:
        aToX = json.load(f)

    with open("refs/xToAlpha.json", "r") as f:
        xToA = json.load(f)


    def __init__(self, **kwargs):
        try:

            self.initLink = kwargs.get('init_link')

        except (KeyError, AttributeError):

            pass


        self._links = []
        self.__links = []
        self.bufferSize = lM.config.get("threads")  # Quantidade de links que precisa ter já prontos
        self.bufferBufferSize = lM.config.get("bb_size")
        self.overWriteLink = None
    @staticmethod
    def __urlToCode(url):
        sp = url.split("/")
        l = len(sp)
        return sp[l - 1]

    @staticmethod
    def __convertAToX(alpha_array):
        tempXArray = []
        for elem in alpha_array:
            tempXArray.append(lM.aToX.get(elem))
        return tempXArray

    @staticmethod
    def __convertXToA(x_array):
        tempAlphaArray = []
        for elem in x_array:
            tempAlphaArray.append(lM.xToA.get(elem))
        return tempAlphaArray

    @staticmethod
    def __assembleAlphaArrToString(alpha_array):
        string = ""
        for alpha in alpha_array:
            string += alpha
        return string

    @staticmethod
    def _genNextURL(old_url):

        code = lM.__urlToCode(old_url)
        chars = [char for char in code]
        idx_actual_char = len(chars)-1

        new_ac_nums = lM.__convertAToX(chars)

        should_increase_next = False

        while -1 < idx_actual_char < len(chars):

            ac_num = int(lM.aToX.get(str(chars[idx_actual_char])))

            if idx_actual_char == len(chars)-1:

                ac_num += 1
                new_ac_nums[idx_actual_char] = str(ac_num)
            elif should_increase_next:
                ac_num += 1
                new_ac_nums[idx_actual_char] = str(ac_num)


            if ac_num >= lM.max_digit_range+1:
                new_ac_nums[idx_actual_char] = "0"
                should_increase_next = True
            else:
                should_increase_next = False

            idx_actual_char -= 1
        return lM.__assembleAlphaArrToString(lM.__convertXToA(new_ac_nums))


    def _genRemainingBuffer(self):
        temp_links = self._links
        last_link = ""


        if self.overWriteLink is None or self.overWriteLink is "":
            try:
                if temp_links[len(temp_links)-1] is not None or temp_links[len(temp_links)-1] is not "":

                    last_link = temp_links[len(temp_links)-1]

            except IndexError:

                pass
            if last_link == "" or last_link is None:

                last_link = self.initLink
        elif self.overWriteLink is not None or self.overWriteLink is not "":


            last_link = self.overWriteLink
            self.overWriteLink = None

        # print("Last Link: " + last_link)




        if not self._links:  # Se vazia

            # print("Aqui Alpha")
            for i in range(1, self.bufferSize+self.bufferBufferSize):  # Mais um para ser o num exato ex: bf = 30, ent 30 links
                if not temp_links:
                    temp_link = lM._genNextURL(last_link)
                    # print("Adding link #" + str(i) + " : " + temp_link)
                    temp_links.append(temp_link)
                if not not temp_links:
                    temp_link = lM._genNextURL(temp_links[len(temp_links)-1])
                    # print("Adding link #" + str(i) + " : " + temp_link)
                    temp_links.append(temp_link)

        else:
            # print("Aqui B")
            for i in range(1, (self.bufferSize+self.bufferBufferSize) - len(self._links)):
                temp_link = lM._genNextURL(last_link)
                # print("Adding link #" + str(i) + " : " + temp_link)
                temp_links.append(temp_link)



        return temp_links

    def overWriteBase(self, over_write_link):
        self.overWriteLink = over_write_link


    def _checkIfAnyLinkIsUsed(self):
        # print(
        # """
        #    self._links : {0},
        #    self.__links: {1}
        # """.format(self._links, self.__links))
        if not self.__links:
            self.__links = self._links
            return

        for link in self._links:  # se o link esta na ref

            if link not in self.__links:  # mas nao no workspace
                idx = self._links.index(link)  # ver em que lugar ele esta na ref
                self._links.pop(idx)  # e retirar


    def retrieveLinkForWork(self):
        self.checkBuffer()

        linkToRetrieve = self.__links[0]

        # print("**Retrieving: ** " + str(lM.url_prefix + linkToRetrieve))
        self.__links.pop(0)
        return lM.url_prefix + linkToRetrieve



    def checkBuffer(self):

        # print(
        #     """\nself._links : {0},\nself.__links: {1}\n""".format(self._links, self.__links))
        # print("_links vazia?: " + str(not self.__links) )

        #       2 links             3-1 + 1
        # print("\nBSize = {0},\nBBSize = {1}\n".format(self.bufferSize, self.bufferBufferSize))
        if len(self._links) < self.bufferSize-1 + self.bufferBufferSize:  # -1 experimental

            self._links = self._genRemainingBuffer()
            self._checkIfAnyLinkIsUsed()
            # print(
            #     """
            #         self._links : {0},
            #         self.__links: {1}
            #     """.format(self._links, self.__links))
        self.__links = self._links


