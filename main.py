import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("adult.csv")
data.columns = ["age", "workclass", "Id", "education", "educational-num","marital-status","occupation", "relationship", "race", "gender", "capital-gain", 
                "capital-loss", "hours-per-week", "native-country", "income"]

data.rename(columns={
 "capital-gain" : "capital gain",
 "capital-loss" : "capital loss",
 "educational-num" : "educational num",
  "marital-status" : "marital",
  "hours-per-week" : "working hours per week",
  "native-country" : "country"

}, inplace=True)

print(data.head(10))
print(data.info())

data.drop(["educational num","age","working hours per week", "Id", "capital gain", "capital loss","country"
], axis = 1,inplace = True)

print(data.head(10))
print(data.isin(["?"]).sum(axis=0))

income = set(data["income"])
print(income)

#mapping the data into numerical data using map function

data["income"] = data["income"].map({" <=50K":0," >50K":1}).astype(int)

print(data.head(10))
#gender
gender = set(data["gender"])
print(gender)

data["gender"] = data["gender"].map({" Male":0," Female":1}).astype(int)
print(data.head(10))

data.groupby("gender").income.mean().plot (kind = "bar") 
plt.show()

#race
race = set(data["race"])
print(race)

data["race"] = data["race"].map({' White':0, ' Amer-Indian-Eskimo':1, ' Black':2, ' Asian-Pac-Islander':3, ' Other':4}).astype(int)
data.groupby("race").income.mean().plot (kind="bar")
plt.show()

#relationship
relationship = set(data["relationship"])
print(relationship)

data["relationship"] = data["relationship"].map({' Own-child':1, ' Wife':2, ' Unmarried':3, ' Other-relative':4, ' Not-in-family':5, ' Husband':6})
data.groupby("relationship").income.mean().plot (kind="bar")
plt.show()
