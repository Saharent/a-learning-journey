words = ["i", "love", "nlp", "very", "much"]


def get_context(words, index):
    result=[]
    result.append(words[index-1])
    result.append(words[index+1])
    return result



vec=get_context(words, 2)
print(vec)
