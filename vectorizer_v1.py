from bag_of_words_v1 import *
import string


def vectorize(text : str, vocab : list):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    text = text.split()
    vector = []

    
    for word in vocab :
        count =0
        for word2 in text:
           if word == word2:
               count += 1
        vector.append(count)       
    return vector



        
       
    

# text= " I LOve NLP"
# vocab = ["i","love","nlp","python"]

# result= vectorize(text,vocab)
# print(result)