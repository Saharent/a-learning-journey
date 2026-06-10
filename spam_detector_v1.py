

spam_words = [
    "free",
    "win",
    "prize",
    "money"
]

def detect_spam(message):
    for i in range(len(spam_words)) :
        if spam_words[i] in message:
            return "SPAM"
        
    return "NOT SPAM"


    
print(detect_spam("I LOVE YOU"))