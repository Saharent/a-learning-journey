from bag_of_words_v1 import*

spam_words = [
    "free",
    "win",
    "prize",
    "money"
]

entered_txt = input("enter a text :\n")

bag = Bag_of_words(entered_txt)


def detect_spam(bag):
    spam_score = 0
    for word in spam_words:
        spam_score += bag.get(word, 0)
    
    return "SPAM" if spam_score > 1 else "NOT SPAM"







