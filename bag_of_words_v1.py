
text = ' I love NLP'


def bag_of_words(text: str):
    text = text.lower()
    words= text.split()
    bag = {}
    for word in words :
        if word in bag :
            bag[word] += 1
        else :
            bag[word] = 1

    return bag


#print(Bag_of_words(text))

def most_common_word(text) :
    bag= bag_of_words(text)
    max = 0
    common = ""
    for word,count in bag.items() :
        if count > max :
            max = count
            common = word
    if common :
        return f'"{common}" : {max}'
    else:
        return "no words found"

