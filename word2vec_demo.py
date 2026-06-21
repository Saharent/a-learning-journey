from gensim.models import Word2Vec

sentences = [
    ["cat", "drink", "milk"],
    ["dog", "drink", "milk"],
    ["cat", "animal"],
    ["dog", "animal"]
]

model = Word2Vec(
    sentences,
    vector_size=10,
    window=2,
    min_count=1
)

#print(model.wv["cat"])
#print(model.wv.most_similar("milk"))
#print(len(model.wv["cat"]))

def word_exists(model, word):
    return word in model.wv

def get_vector(model, word):
    if word in model.wv:
        return model.wv[word]
    else:
        return None
def similarity(model, word1, word2):
    if word1 in model.wv and word2 in model.wv:
        return model.wv.similarity(word1, word2)
    return None

