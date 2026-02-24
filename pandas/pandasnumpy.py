import array

import pandas as pd
import numpy as np

names = [
    'Alexander', 'Maria', 'Dmitry', 'Elena', 'Maxim', 
    'Anna', 'Sergey', 'Olga', 'Ivan', 'Natalia'
]

math = np.random.randint(2, 6, size=10)
physics = np.random.randint(2, 6, size=10)
english = np.random.randint(2, 6, size=10)
age = np.random.randint(15, 19, size=10)
attendance = np.random.randint(20, 101, size=10)


df = pd.DataFrame (
    {
        "Names": names,
        "Math": math,
        "Physics": physics,
        "English": english,
        "Age": age,
        "Attendance %": attendance
    })
print(df)
    


