import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# 1. Load the cleaned CSV
# -------------------------------
cleaned_file = r"D:\New folder\eda_project\data\processed\students_cleaned.csv"
df = pd.read_csv(cleaned_file)

print("Dataset Loaded Successfully!\n")
print(df.head())

# -------------------------------
# 2. Summary Statistics
# -------------------------------
print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Categorical Columns Info ---")
categorical_cols = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
for col in categorical_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

# -------------------------------
# 3. Histograms for Numeric Columns
# -------------------------------
numeric_cols = ['math score', 'reading score', 'writing score']
plt.figure(figsize=(12, 4))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[col], bins=10, kde=True, color='skyblue')
    plt.title(f'{col} Distribution')
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Boxplots to Check Scores by Gender
# -------------------------------
plt.figure(figsize=(12, 4))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x='gender', y=col, data=df, palette='Set2')
    plt.title(f'{col} by Gender')
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Score Correlation Heatmap
# -------------------------------
plt.figure(figsize=(8, 6))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Scores")
plt.show()

# -------------------------------
# 6. Test Preparation Effect
# -------------------------------
plt.figure(figsize=(12, 4))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(x='test preparation course', y=col, data=df, palette='Pastel1')
    plt.title(f'{col} vs Test Prep Course')
plt.tight_layout()
plt.show()

# -------------------------------
# 7. Save Plots (Optional)
# -------------------------------
output_folder = r"D:\New folder\eda_project\outputs"
os.makedirs(output_folder, exist_ok=True)
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], bins=10, kde=True, color='skyblue')
    plt.title(f'{col} Distribution')
    plt.savefig(os.path.join(output_folder, f'{col}_distribution.png'))
    plt.close()

print("\nEDA Completed! Plots saved to 'outputs/' folder.")