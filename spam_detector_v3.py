from vectorizer_v1 import *

SPAM_VOCAB = ["free", "win", "money", "prize"]

def detect_spam(input_text, vocab):


    vector = vectorize(input_text, vocab)
    
    score = sum(vector) 

    if score > 1:
        return "SPAM"
    else:
        return "NOT SPAM"

# user_input = input("Enter a text : \n")
# result = detect_spam(user_input, SPAM_VOCAB)
# print(f"Result: {result}")














