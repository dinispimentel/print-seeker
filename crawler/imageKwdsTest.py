


from new.kwdFinder import kF
from new.lightGet import lG

lg = lG("https://prnt.sc/1uwluu9")  # 1uwluu8
image = lg.getImage()

kf = kF(image)

kf.findKeywords()
print("Text: " + str(kf.text))
print(kf.kwds)
