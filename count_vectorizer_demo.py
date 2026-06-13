from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "I love NLP",
    "I love Python",
    "Python is great"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

print("Vocabulary:")
print(vectorizer.vocabulary_)

print("\nMatrix:")
print(X.toarray())