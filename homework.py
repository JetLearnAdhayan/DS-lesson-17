import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("car.data")
data.columns = ["col1", "col2","col3","col4","col5","col6","col7"]

print(data.head(10))
print(data.info())

col1 = set(data["col1"])
print(col1)

col2 = set(data["col2"])
print(col2)

col3 = set(data["col3"])
print(col3)

col4 = set(data["col4"])
print(col4)

col5 = set(data["col5"])
print(col5)

col6 = set(data["col6"])
print(col6)

col7 = set(data["col7"])
print(col7)
