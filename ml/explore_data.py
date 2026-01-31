print("SCRIPT STARTED")

import pandas as pd

file_path = "../data/healthcare_noshows_appt.csv"
df = pd.read_csv(file_path)

print(df.head())
print(df.info())
