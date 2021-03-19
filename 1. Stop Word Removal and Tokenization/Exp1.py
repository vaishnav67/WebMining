import re
stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
f = open("paragraph.txt").read()
print('Paragraph:'+'\n'+f)
print('Paragraph after removal of stop words:')
for sw in stop_words:
    f = re.sub(r'[^\w\s]|\b'+re.escape(sw)+r'\b','',f)
print(f)

import re
stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
sen = "This is a sentence made out of words."
for sw in stop_words:
    sen = re.sub(r'[^\w\s]|\b'+re.escape(sw)+r'\b',' ',sen)
sen=sen.split()
print(sen)

import re
stop_words = ['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to',]
f = open("paragraph.txt").read()
print('Paragraph:'+'\n'+f)
sentenceEnders = re.compile('[.!?][\s]{1,2}')
sentences = sentenceEnders.split(f)
print("Changed paragraph to sentences:")
print(sentences)
print('Tokenization of sentences with stop words removed:')
for i in range(0,len(sentences)):
    for sw in stop_words:
        sentences[i] = re.sub(r'[^\w\s]|\b'+re.escape(sw)+r'\b','',sentences[i])
    print(sentences[i].split())
