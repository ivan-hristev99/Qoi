from bs4 import BeautifulSoup
import requests
from googlesearch import search  

class WebScrapper:

    def __init__(self):
        print("Web scraping initialized...")

    def webScrape(self, webList):
        toSummarize = ""
        text = ""

        #print(webList)
        for x in webList:
            if "wikipedia" in x:
                #print('wiki')
                source = requests.get(x).text
                soup = BeautifulSoup(source, 'lxml')
                #print(soup)
                response = requests.get(x)
                html = BeautifulSoup(response.text, 'html.parser')

                title = html.select("#firstHeading")[0].text
                paragraphs = html.select("p")
                #print(paragraphs)
                allText = '\n'.join([para.text for para in paragraphs])
                toSummarize += " " + allText
            else:
                print('no wiki')

        print(toSummarize)
        return(toSummarize)

    
    




