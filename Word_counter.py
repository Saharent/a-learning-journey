import re

def clean_txt(s):

    return re.sub(r'[^\w\s]', '', s)

def to_words(cleaned_text):
    
    return re.findall(r'\b\w+\b', cleaned_text)

def num_of_uniques(s):
    s = s.lower()
    cleaned_text = clean_txt(s)
    words = to_words(cleaned_text)
    unique_words = set(words)
    return len(unique_words)

def frequent_words(s):

    s = s.lower()
    cleaned_text = clean_txt(s)
    words = to_words(cleaned_text)

    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1


    sorted_words = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    top_three = sorted_words[:3]
    for word, count in top_three:
        print(f"'{word}': {count}")

# test_text = "Python is great, and learning Python is fun! Python is powerful."
# print(f"number of unique words: {num_of_uniques(test_text)}")
# frequent_words(test_text)
