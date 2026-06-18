words = ["i", "love", "nlp", "very", "much"]


def get_context(words, index, window_size=2):
    result =[]
    start = max(0, index - window_size)
    end = min(len(words), index+window_size+1)
    for i in range(start , end):
        if i != index :
            result.append(words[i])
    return result

# vec = get_context(words, 3 , 1)
# print(vec)