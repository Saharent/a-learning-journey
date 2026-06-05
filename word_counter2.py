from collections import Counter
import re


def average_word_length(text):
    words = process(text)
    
    lengths = []

    for word in words:
        lengths.append(len(word))

    return sum(lengths) / len(lengths)



def clean_txt(s):

    return re.sub(r'[^\w\s]', '', s)

def to_words(cleaned_text):
    
    return re.findall(r'\b\w+\b', cleaned_text)


def process(s):
    s = s.lower()
    cleaned_text = clean_txt(s)
    words = to_words(cleaned_text)
    return words



def frequent_words_pro(s):
    words=process(s)
    count_dict=Counter(words)
    return count_dict


def num_of_uniques(s):
    words=process(s)
    unique_words = set(words)
    return len(unique_words)



def lexical_diversity(text):
    uniques=num_of_uniques(text)
    all_words= process(text)
    num_of_all=len(all_words)
    return uniques/num_of_all




#test-------------------------------

# test_text = "apple orange apple banana orange apple"
# print(frequent_words_pro(test_text))


