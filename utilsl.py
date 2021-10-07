


class UtilsL:

    @staticmethod
    def checkListEmpty(l):

        veredict = False

        if l is None:
            return True
        if len(l) == 0:
            return True
        else:

            for elem in l:
                if type(elem) == str:
                    if elem == "" or elem == '[]':
                        veredict = True
                if type(elem) == list:
                    veredict = UtilsL.checkListEmpty(elem)

            return veredict
