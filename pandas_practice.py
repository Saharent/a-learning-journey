import pandas as pd

students = {
    "hours": [2, 3, 5, 8],
    "passed": [0, 0, 1, 1]
}

df = pd.DataFrame(students)

print(df)
print(df.shape)
print(df.columns)
print(df.head())