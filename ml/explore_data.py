print("SCRIPT STARTED")

import pandas as pd

file_path = "../data/healthcare_noshows_appt.csv"

df = pd.read_csv(file_path)

print("DATA LOADED SUCCESSFULLY")
print("First 5 rows:")
print(df.head())

print("\nDATA INFO:")
print(df.info())

print("SCRIPT FINISHED")
