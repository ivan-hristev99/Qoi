# Input Processor v0.1 ALPHA
# 30/11/2019 14:27
#
#

from speechToText import *
from WebParser import *
from summariser import *
import spacy
from spacy.symbols import nsubj, VERB

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

#Process whole documents
text = input("QOI: Hi there, how can I help? ")
#s1 = SpeechToText()
#text = s1.recognizeSpeech()

doc = nlp(text)
output = set()

for token in doc:
    print(token.text, token.pos_, token.dep_)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
          
# Finding a verb with a subject from below — good
verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)

# Refining text
nouns = [chunk.text for chunk in doc.noun_chunks]
arrayOfEntities = []

for entity in doc.ents:
    output.add(entity.text)

if arrayOfEntities:
    for entity in doc.ents:
        nouns.remove(entity.text)
    
if nouns:
    longestChunk = (max(nouns, key=len))
    output.add(longestChunk)


for token in doc:
    if token.pos_=="VERB":
        if token.dep_!="xcomp":
            if token.lemma_!="tell":
                if token.lemma_!="give":
                    output.add(token.lemma_)

if not output:
    biggestNoun=max(nouns, key=len)
    if biggestNoun != "me" :
        output.add(biggestNoun)

          
print(output)

# google search
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search
query = ""
for x in output:
    query += " " + x


print(query)

urlArrayList = []

wikiFound = False;
for url in search(query, stop=7):
    if 'wikipedia' in url:
        if (wikiFound == False):
            wikiFound = True;
            urlArrayList.append(url)
    else:
        urlArrayList.append(url)

print(urlArrayList)

w1 = WebScrapper()
webStrings = w1.webScrape(urlArrayList)

summarise1 = Summarizer()
outputResult = summarise1.summarize(webStrings)

#print(webStrings)
print(outputResult)

print("Statistics:")
print("Web scrapping scrapped ",len(webStrings)," chars.");
print("Summarizer summarized it to " ,len(outputResult), " chars.");



'''
# GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *

window = Tk()
window.title("Qoi")
window.geometry('800x640')

style = ttk.Style(window)
style.configure('lefttab.TNotebook',tabposition='wn')

tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1,text=f'{"Home":^22}')
tab_control.add(tab2,text=f'{"About":^22}')
tab_control.pack(expand=1,fill='both')

#'Home' page
l1 = Label(tab1,text='Welcome to Qoi! Enter a question', padx=5, pady=5)
l1.grid(row=1,column=0)
inputField = ScrolledText(tab1, height=3)
inputField.grid(row=2,column=0,columnspan=2,pady=5,padx=5)

l2 = Label(tab1, text='Number of sentences in summary:',padx=5,pady=5)
l2.grid(row=4,column=0)
numField = Entry(tab1)
numField.grid(row=4,column=1)

b1 = Button(tab1,text='Submit',width=10,bg='#000000',fg='#000000', command=summarize)
b1.grid(row=5,column=1,padx=10,pady=10)

l3 = Label(tab1,text='Result', padx=5, pady=5)
l3.grid(row=6,column=0)
result = ScrolledText(tab1,height=10)
result.grid(row=7,column=0,columnspan=3,padx=5,pady=5)
'''





















