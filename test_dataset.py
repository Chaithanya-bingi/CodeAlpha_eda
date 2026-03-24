import pandas as pd
import os

print("Current Working Directory:", os.getcwd())

df = pd.read_csv("data/raw/students.csv")

print("\nDataset Loaded Successfully!\n")
print(df.head())