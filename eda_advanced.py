import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# 1. Load the cleaned CSV
# -------------------------------
cleaned_file = r"D:\New folder\eda_project\data\processed\students_cleaned.csv"
df = pd.read_csv(cleaned_file)

print("Cleaned dataset loaded successfully!\n")

# Ensure outputs folder exists
output_folder = r"D:\New folder\eda_project\outputs"
os.makedirs(output_folder, exist_ok=True)

# -------------------------------
# 2. Pairplot for numeric scores
# -------------------------------
sns.set(style="ticks")
pairplot_file = os.path.join(output_folder, "pairplot_scores.png")
plt.figure()
sns.pairplot(df, vars=['math score', 'reading score', 'writing score'], hue='gender', palette='Set1')
plt.savefig(pairplot_file)
plt.close()
print(f"Pairplot saved to: {pairplot_file}")

# -------------------------------
# 3. Violin plots for scores vs categorical variables
# -------------------------------
categorical_cols = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
numeric_cols = ['math score', 'reading score', 'writing score']

for cat_col in categorical_cols:
    for num_col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.violinplot(x=cat_col, y=num_col, data=df, palette='Pastel2')
        plt.title(f'{num_col} vs {cat_col}')
        plt.xticks(rotation=45)
        
        # Replace invalid characters in filename
        safe_cat = cat_col.replace(" ", "_").replace("/", "_").replace("\\", "_")
        safe_num = num_col.replace(" ", "_")
        filename = os.path.join(output_folder, f"violin_{safe_num}_{safe_cat}.png")
        
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Violin plot saved to: {filename}")

# -------------------------------
# 4. Boxplots for test preparation course
# -------------------------------
for num_col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='test preparation course', y=num_col, data=df, palette='Set3')
    plt.title(f'{num_col} vs Test Preparation Course')
    
    # Safe filename
    safe_num = num_col.replace(" ", "_")
    filename = os.path.join(output_folder, f"boxplot_{safe_num}_testprep.png")
    
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Boxplot saved to: {filename}")

# -------------------------------
# 5. Completion
# -------------------------------
print("\nAdvanced EDA Completed!")
print(f"All plots saved to '{output_folder}' folder.")