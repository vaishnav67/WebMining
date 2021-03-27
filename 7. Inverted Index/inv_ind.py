import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def tokenize(file):
    read = file.read()
    file.seek(0)
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in read:  
        if ele in punc:  
            read = read.replace(ele, " ")       
    read=read.lower()                    
    for i in range(1):
        text_tokens = word_tokenize(read)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words("english")]
    return tokens_without_sw
def idf(doc,item,tokens,dict):
    i=0
    count=0
    t=[]
    if item in tokens:
        for it in tokens:
            i+=1
            if it==item:
                count+=1
                if item not in dict:
                        dict[item] = []
                if item in dict:
                        t.append(i)
        dict[item].append(["d"+str(doc),count,t])
    return (dict)
file1 = open('rhythm1.txt', encoding='utf8')
file2 = open('rhythm2.txt', encoding='utf8')
file3 = open('rhythm3.txt', encoding='utf8')
tokens1=tokenize(file1)
tokens2=tokenize(file2)
tokens3=tokenize(file3)
tokens=tokens1+tokens2+tokens3
temp=[]
for x in tokens:
    if x not in temp:
        temp.append(x)
print("Output A:")
for i in temp:
    print("\n"+i+":",end=" ")
    if(i in tokens1):
        print("d1",end=" ")
    if(i in tokens2):
        print("d2",end=" ")
    if(i in tokens3):
        print("d3",end=" ")
print("\n\nOutput B:\n")
dict = {}
for item in temp:
    dict=idf(1,item,tokens1,dict)
    dict=idf(2,item,tokens2,dict)
    dict=idf(3,item,tokens3,dict)
for i in dict:
    print (i+":"+str(dict[i]))
