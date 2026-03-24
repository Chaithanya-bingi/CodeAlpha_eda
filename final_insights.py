import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv(r"D:\New folder\eda_project\data\processed\students_cleaned.csv")

print("Dataset Loaded Successfully!\n")

# Create outputs folder if not exists
output_path = r"D:\New folder\eda_project\outputs"
os.makedirs(output_path, exist_ok=True)

# -------------------------------
# 1. Correlation Heatmap
# -------------------------------

plt.figure(figsize=(8,6))

corr = df[['math score','reading score','writing score']].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Between Scores")

heatmap_file = os.path.join(output_path, "correlation_heatmap.png")

plt.savefig(heatmap_file)
plt.close()

print("Correlation heatmap saved:", heatmap_file)


# -------------------------------
# 2. Average Scores by Gender
# -------------------------------

plt.figure(figsize=(8,6))

gender_scores = df.groupby("gender")[['math score','reading score','writing score']].mean()

gender_scores.plot(kind="bar")

plt.title("Average Scores by Gender")
plt.ylabel("Average Score")

gender_file = os.path.join(output_path,"avg_scores_gender.png")

plt.savefig(gender_file)

plt.close()

print("Gender comparison plot saved:", gender_file)


# -------------------------------
# 3. Test Preparation Impact
# -------------------------------

plt.figure(figsize=(8,6))

prep_scores = df.groupby("test preparation course")[['math score','reading score','writing score']].mean()

prep_scores.plot(kind="bar")

plt.title("Impact of Test Preparation Course")
plt.ylabel("Average Score")

prep_file = os.path.join(output_path,"testprep_impact.png")

plt.savefig(prep_file)

plt.close()

print("Test preparation plot saved:", prep_file)


# -------------------------------
# 4. Lunch Type Impact
# -------------------------------

plt.figure(figsize=(8,6))

lunch_scores = df.groupby("lunch")[['math score','reading score','writing score']].mean()

lunch_scores.plot(kind="bar")

plt.title("Impact of Lunch Type on Scores")
plt.ylabel("Average Score")

lunch_file = os.path.join(output_path,"lunch_impact.png")

plt.savefig(lunch_file)

plt.close()

print("Lunch impact plot saved:", lunch_file)


print("\nStep 7 Completed Successfully!")