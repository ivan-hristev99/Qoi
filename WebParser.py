
from lxml import html
import requests

class WebScrapper:

    def __init__(self):
        print("Web scraping initialized...")

    def webScrape(self, webList):
        toSummarize = ""
        text1 = ""
        for url in webList:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            text1 = tree.xpath('//p/text()')
            #text2 = tree.xpath('//a/text()')
            for x in text1:
                if (len(toSummarize) < 1500):
                    toSummarize += " " + x
                else:
                    break
            #for a in text2:
               # toSummarize += " " + a
            


        return(toSummarize)



