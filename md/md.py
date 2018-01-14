# encoding utf-8

import html2text
import os

files = os.listdir("../../tool/file/")
newFile = "../../tool/mdfile/"

for f in files:
    with open("../../tool/file/" + f, encoding='utf-8') as lines:
        lList = lines.readlines()
        lStr = ""
        for s in lList:
            lStr += s
        start = lStr.find("<article")
        end = lStr.find('<div class="post-copyright">')
        article = lStr[start: end]+"</article>"
        mdfile = html2text.html2text(article)
        f2 = open(newFile+f[0:-4]+"md", 'w', encoding='utf-8')
        f2.write(mdfile)
