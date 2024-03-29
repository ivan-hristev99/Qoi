import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


class Summarizer:
    def __init__(self):
        print("Summarizer is being initiallized...")

    def summarize(self, text):
       # test1 = inputField.get('1.0', tk.END)
        #test2 = numField.get()
        #print(test1)
        #print(test2)

        stopwords = list(STOP_WORDS)

       # document1 ="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""
        document1 = text
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

        #print(word_frequencies)

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

        summarized_sentences = nlargest(5, sentence_scores, key=sentence_scores.get)

        #print(summarized_sentences)

        final_sentences = [ w.text for w in summarized_sentences ]

        summary = ' '.join(final_sentences)
        print("---------")
        print(document1)
        print("---------")
        #print(summary)
        return summary













