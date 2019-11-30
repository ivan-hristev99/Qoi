# Input Processor v0.1 ALPHA
# 30/11/2019 14:27
#
#

from speechToText import *
from WebParser import *
import spacy
from spacy.symbols import nsubj, VERB

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
# text = input("QOI: Hi there, how can I help? ")
s1 = SpeechToText()
text = s1.recognizeSpeech()

doc = nlp(text)
arrayOfChunks = [chunk.text for chunk in doc.noun_chunks]
longestChunk = (max(arrayOfChunks, key=len))

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

output = set()
for entity in doc.ents:
    output.add(entity.text)

for token in doc:
    if token.pos_=="VERB":
        if token.dep_!="xcomp":
                output.add(token.lemma_)
        
print(output)

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

for url in search(query, stop=3): 
    urlArrayList.append(url)

print(urlArrayList)

w1 = WebScrapper()
webStrings = w1.webScrape(urlArrayList)

print(webStrings)





















