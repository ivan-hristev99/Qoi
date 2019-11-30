# Input Processor v0.1 ALPHA
# 30/11/2019 14:27
#
#


import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = input("QOI: Hi there, how can I help? ")

doc = nlp(text)

for token in doc:
    print(token.text, token.pos_, token.dep_)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
