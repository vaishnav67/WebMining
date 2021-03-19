from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
example_sent = "My name is Vaishnav Santhosh and I like programing, watching movies, tv shows and playing games."
stop_word = set(stopwords.words('english')+['.',','])
word_tokens = word_tokenize(example_sent)  
filtered_words = [word for word in word_tokens if word not in stop_word]
print(filtered_words)

import nltk
stop_word = set(stopwords.words('english')+['.',','])
text=open("paragraph.txt").read()
print("Paragraph:"+"\n"+text)
para=nltk.sent_tokenize(text)
print("Paragraph to sentences:")
print(para)
print("Sentences tokenized:")
for sentence in para:
    tokenized_text = nltk.word_tokenize(sentence)
    tokenized_text = [word for word in tokenized_text if word not in stop_word]
    print(tokenized_text) 
