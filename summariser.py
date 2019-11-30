import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


stopwords = list(STOP_WORDS)


document1 = open 
nlp = spacy.load('en_core_web_sm')

docx = nlp(document1)
mytokens = [token.text for token in docx]



word_frequencies = {}
for word in docx:
    if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

##print(word_frequencies)

sentence_list = [ sentence for sentence in docx.sents ]

sentence_scores = {}  
for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

#print(sentence_scores)

summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)

#print(summarized_sentences)

for w in summarized_sentences:
    print(w.text)

final_sentences = [ w.text for w in summarized_sentences ]

summary = ' '.join(final_sentences)

print(document1)
print("---------")
print(summary)








