from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

messages = [
    "free money now",
    "win a free prize",
    "hello my friend",
    "how are you",
    "claim your money",
    "good morning",
    "free free free money",
    "nice to meet you"
]

labels = [1, 1, 0, 0, 1, 0, 1, 0]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(messages)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.25,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

new_message = ["hello friend"]


new_vector = vectorizer.transform(new_message)

prediction = model.predict(new_vector)

print(prediction)