from sklearn.linear_model import LogisticRegression



X = [
    [2, 3],   # study_hours, talent
    [3, 4],
    [5, 6],
    [8, 8],
    [10, 9]
]

y = [0, 0, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

prd1 = model.predict([[1,3]])
prd2 = model.predict([[2,9]])
prd3 = model.predict([[10,3]])
prd4 = model.predict([[8,9]])

print(f'{prd1} \n {prd2} \n {prd3} \n {prd4}')