import array
from pydoc import describe

import pandas as pd
import numpy as np

names = [
    'Alexander', 'Maria', 'Dmitry', 'Elena', 'Maxim', 
    'Anna', 'Sergey', 'Olga', 'Ivan', 'Natalia'
]

math = np.random.randint(2, 6, size=10)
physic = np.random.randint(2, 6, size=10)
english = np.random.randint(2, 6, size=10)
age = np.random.randint(15, 19, size=10)
attendance = np.random.randint(20, 101, size=10)


df = pd.DataFrame (
    {
        "Names": names,
        "Math": math,
        "Physic": physic,
        "English": english,
        "Age": age,
        "Attendance %": attendance
    })
print(df)

print("-------------------------------------------------------")

start = df.head()
print(start)

print("-------------------------------------------------------")

describe = df.describe()
print(describe)

print("-------------------------------------------------------")

mean_value_math = df["Math"].mean()
mean_value_phycic = df["Physic"].mean()
mean_value_english = df["English"].mean()

df_mean = pd.DataFrame(
    {
        "Math_mean_value": [mean_value_math],
        "Phycic_mean_value": [mean_value_phycic],
        "English_mean_value": [mean_value_english],
    })
print(df_mean)

print("-------------------------------------------------------")

math_four = df.loc[df["Math"] >= 4]
name = math_four[["Names"]]  
print(name)
    
print("-------------------------------------------------------")

print("-------------------------------------------------------")

df["Average"] = (df["Math"] + df["Physic"] + df["English"])/3
df["Average"] = df["Average"].round(2)
print(df)

print("-------------------------------------------------------")

good = df.loc[df["Average"] >= 4.5]
if good.empty:
    print("Not find")
else:
    name2 = good[["Names"]]  
    print(name2)


print("-------------------------------------------------------")

df_sort = df.sort_values(by="Average", ascending=False)
print(df_sort)

df.to_csv("results.csv", index=False, encoding='utf-8-sig')



