import clipboard as clip
import wikipedia as wiki
import os , textwrap, time

wrap = textwrap.TextWrapper(width = 80)
a = False

while a == False:
    text = clip.paste()
    text3 = text[0:3]
    if text3 == "lu!":
        text4 = text[3:]
        try:
            text2 = wiki.summary(text4)
            with open('wiki.txt', 'w') as x:
                x.write(wrap.fill(text2))
            os.startfile("wiki.txt")
            clip.copy(text4)
        except:
            with open('wiki.txt', 'w') as x:
                x.write("Error: Either check your spelling or try to be more specific")
            os.startfile("wiki.txt")
            text4 = text[3:]
            clip.copy(text4)
    elif text3 == "stp":
        text4 = text[3:]
        clip.copy(text4)
        a = True
    time.sleep(1)