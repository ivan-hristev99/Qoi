
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
            for x in text1:
                toSummarize += " " + x            
            


        return(toSummarize)



