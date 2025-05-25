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

data.drop(["educational num","age","working hours per week", "Id", "capital gain", "capital loss"
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

data["relationship"] = data["relationship"].map({' Own-child':1, ' Wife':2, ' Unmarried':3, ' Other-relative':4, ' Not-in-family':5, ' Husband':6}).astype(int)
data.groupby("relationship").income.mean().plot (kind="bar")
plt.show()

#homework
#country
country = set(data["country"])
print(country)

data["country"] = data["country"].map({'Scotland':1, ' ?':2, ' Yugoslavia':3, ' Hungary':4, ' Hong':5, ' Italy':6, ' France':7, ' South':8, ' Japan':9, ' Outlying-US(Guam-USVI-etc)':10, ' Guatemala':11, ' Cambodia':12, ' Trinadad&Tobago':13, ' Iran':14, ' El-Salvador':15, ' Nicaragua':16, ' Laos':17, ' Holand-Netherlands':18, ' Peru':19, ' United-States':20, ' Greece':21, ' Cuba':22, ' Portugal':23, ' Puerto-Rico':24, ' Ecuador':25, ' Germany':26, ' Canada':27, ' Columbia':28, ' India':29, ' Jamaica':30, 
' Haiti':31, ' Thailand':32, ' Poland':33, ' Dominican-Republic':34, ' Ireland':35, ' Vietnam':36, ' Philippines':37, ' Taiwan':38, ' China':39, ' Mexico':40, ' England':41, ' Honduras':42})

data.groupby("country").income.mean().plot(kind = "bar")
plt.show()

print(data.head())

#occupation
occupation = set(data["occupation"])
print(occupation)

data["occupation"] = data["occupation"].map({' Adm-clerical':1, ' Transport-moving':2, ' Sales':3, ' Armed-Forces':4, ' Prof-specialty':5, ' Craft-repair':6, 
' Protective-serv':7, ' Tech-support':8, ' ?':9, ' Exec-managerial':10, ' Other-service':11, ' Priv-house-serv':12, ' Handlers-cleaners':13, ' Machine-op-inspct':14, 
' Farming-fishing':15})

data.groupby("occupation").income.mean().plot(kind = "bar")
plt.show()

print(data.head())

#marital
marital = set(data["marital"])
print(marital)

data["marital"] = data["marital"].map({' Never-married':1, ' Separated':2, ' Divorced':3,
   ' Married-spouse-absent':4, ' Widowed':5, ' Married-civ-spouse':6, ' Married-AF-spouse':7})

data.groupby("marital").income.mean().plot(kind = "bar")
plt.show()

print(data.head())

#education
education = set(data["education"])
print(education)

data["education"] = data["education"].map({' 11th':1, ' Preschool':2, ' 12th':3, ' Assoc-voc':4, ' 10th':5, ' 7th-8th':6,
    ' Doctorate':7, ' Bachelors':8, ' Assoc-acdm':9, ' 9th':10, ' HS-grad':11, ' Masters':12, 
  ' Prof-school':13, ' Some-college':14, ' 1st-4th':15, ' 5th-6th':16})

data.groupby("education").income.mean().plot(kind = "bar")
plt.show()

print(data.head())

#workclass
workclass = set(data["workclass"])
print(workclass)

data["workclass"] = data["workclass"].map({' State-gov':1, ' Local-gov':2, ' ?':3, ' Never-worked':4, ' Federal-gov':5,
   ' Self-emp-inc':6, ' Without-pay':7, ' Private':8, ' Self-emp-not-inc':9})

data.groupby("workclass").income.mean().plot(kind = "bar")
plt.show()

print(data.head())