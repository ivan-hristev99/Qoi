class WebScrapper:

def __init__(self):
    self.list


from lxml import html
import requests


toSummarize = ""

for url in list:
    page = requests.get('url')
    tree = html.fromstring(page.content)
    text = tree.xpath('//p/text()')
    toSummarize += " " + text


print(toSummary)



