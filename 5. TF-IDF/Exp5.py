from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words
import nltk
import os
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re
import math
title = "documents"
alpha = 0.3
folders = [x[0] for x in os.walk(str(os.getcwd())+'/'+title+'/')]
folders[0] = folders[0][:len(folders[0])-1]
dirite=os.listdir(folders[0])
dataset=[]
for i in dirite:
    dataset.append((i,i.strip(".txt")))
def convert_lower_case(data):
    return np.char.lower(data)
def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text
def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data
def remove_apostrophe(data):
    return np.char.replace(data, "'", "")
def stemming(data):
    stemmer= PorterStemmer()
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text
def convert_numbers(data):
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        try:
            w = num2words(int(w))
        except:
            a = 0
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text
def preprocess(data):
    data = convert_lower_case(data)
    data = remove_punctuation(data)
    data = remove_apostrophe(data)
    data = remove_stop_words(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = convert_numbers(data)
    data = stemming(data)
    data = remove_punctuation(data)
    data = remove_stop_words(data)
    return data
N = len (dataset)
processed_text = []
processed_title = []
for i in dataset[:N]:
    file = open(title+'/'+i[0], 'r', encoding="utf8", errors='ignore')
    text = file.read().strip()
    file.close()
    processed_text.append(word_tokenize(str(preprocess(text))))
    processed_title.append(word_tokenize(str(preprocess(i[1]))))
DF = {}
for i in range(N):
    tokens = processed_text[i]
    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i}

    tokens = processed_title[i]
    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i}
for i in DF:
    DF[i] = len(DF[i])
total_vocab_size = len(DF)
total_vocab = [x for x in DF]
def doc_freq(word):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c
doc = 0
tf_idf = {}
for i in range(N):
    tokens = processed_text[i]
    counter = Counter(tokens + processed_title[i])
    words_count = len(tokens + processed_title[i])
    for token in np.unique(tokens):
        tf = counter[token]/words_count
        df = doc_freq(token)
        idf = np.log((N+1)/(df+1))
        tf_idf[doc, token] = tf*idf
    doc += 1
def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim
D = np.zeros((N, total_vocab_size))
for i in tf_idf:
    try:
        ind = total_vocab.index(i[1])
        D[i[0]][ind] = tf_idf[i]
    except:
        pass
def gen_vector(tokens):
    Q = np.zeros((len(total_vocab)))
    counter = Counter(tokens)
    words_count = len(tokens)
    query_weights = {}
    for token in np.unique(tokens):
        tf = counter[token]/words_count
        df = doc_freq(token)
        idf = math.log((N+1)/(df+1))
        try:
            ind = total_vocab.index(token)
            Q[ind] = tf*idf
        except:
            pass
    return Q
def cosine_similarity(k, query):
    print("Cosine Similarity")
    preprocessed_query = preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))
    print("\nQuery:", query)
    print("")
    print(tokens)
    d_cosines = []
    query_vector = gen_vector(tokens)
    for d in D:
        d_cosines.append(cosine_sim(query_vector, d))
    out = np.array(d_cosines).argsort()[-k:][::-1]
    for i in out:
       print(dataset[i][1])
    for i in out:
       print(dataset[i][1]+" is the highest in terms of cosine similarity")
       break
cosine_similarity(5, "Web mining")
def euclid_dist(a, b):
    sum=0
    for i in range(0,len(a)):
        sum+=pow((a[i]-b[i]),2)
    math.sqrt(sum)
    return sum
def euclidean_distance(k,query):
    print("Euclidean Distance")
    preprocessed_query = preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))
    print("\nQuery:", query)
    print("")
    print(tokens)
    euc_dis = []
    query_vector = gen_vector(tokens)
    for d in D:
        euc_dis.append(euclid_dist(query_vector,d))
    out = np.array(euc_dis).argsort()[-k:]
    for i in out:
       print(dataset[i][1])
    for i in out:
       print(dataset[i][1]+" is the highest in terms of euclidean distance")
       break
euclidean_distance(5, "Web mining")
