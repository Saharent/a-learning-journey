from sklearn.linear_model import LogisticRegression

X = [[2], [3], [5], [8], [10]]
y = [0, 0, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

prediction1 = model.predict([[1]])
prediction2 = model.predict([[4]])
prediction3 = model.predict([[7]])
prediction4 = model.predict([[12]])


print(f'{prediction1}\n{prediction2}\n{prediction3}\n{prediction4}')