import os
import pandas as pd

# -------------------------------
# 1. Load dataset using absolute path
# -------------------------------
df = pd.read_csv(r"D:\New folder\eda_project\data\raw\students.csv")

# -------------------------------
# 2. Check for missing values
# -------------------------------
print("Missing values per column:")
print(df.isnull().sum())

missing_percentage = df.isnull().sum() / len(df) * 100
print("\nMissing values percentage per column:")
print(missing_percentage)

# -------------------------------
# 3. Remove duplicates
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# 4. Standardize text columns
# -------------------------------
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.strip().str.upper()

if 'race/ethnicity' in df.columns:
    df['race/ethnicity'] = df['race/ethnicity'].str.strip().str.title()

if 'parental level of education' in df.columns:
    df['parental level of education'] = df['parental level of education'].str.strip().str.title()

if 'lunch' in df.columns:
    df['lunch'] = df['lunch'].str.strip().str.lower()

if 'test preparation course' in df.columns:
    df['test preparation course'] = df['test preparation course'].str.strip().str.lower()

# -------------------------------
# 5. Ensure 'processed' folder exists
# -------------------------------
processed_folder = r"D:\New folder\eda_project\data\processed"
os.makedirs(processed_folder, exist_ok=True)

# -------------------------------
# 6. Save cleaned CSV
# -------------------------------
cleaned_file = os.path.join(processed_folder, "students_cleaned.csv")
df.to_csv(cleaned_file, index=False)

print(f"\nData cleaning complete. Cleaned file saved to:\n{cleaned_file}")