import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
if not os.path.exists("plots"):   #create a plots folder if it doesnt exist
    os.makedirs("plots")


# Load the CSV

df = pd.read_csv("ASK1_Dataset.csv")
print("First 5 rows of dataset:")
print(df.head(), "\n")

print("Column names:")
print(list(df.columns), "\n")

# Clean IC50 values
# In drug discovery, you cant calculate or plot IC50 if the value is missing or in text

df = df.dropna(subset=["standard_value"])  # drop missing IC50
df["standard_value"] = pd.to_numeric(df["standard_value"], errors="coerce")
df = df.dropna(subset=["standard_value"])  # drop invalid IC50
print("Data cleaned. Number of valid rows:", len(df), "\n")    # this shows how many valid rows remains after cleaning


# Summary statistics
# This tells us how potent compounds are on average, and the range of potencies

print("Summary statistics for IC50 (nM):")
print(df["standard_value"].describe(), "\n")

# Mean IC50 per compound
# Compounds with low IC50 values are generally considered good inhibitors because they are highly potent

mean_ic50_per_compound = df.groupby("molecule_chembl_id")["standard_value"].mean()
print("✅ Mean IC50 per compound (top 10):")
print(mean_ic50_per_compound.head(10), "\n")  #just shows the first 10 compounds mean IC50 values for visualisation


# Count measurements per compound
# groups data by unique compound IDs because in the dataframe, there are multiple rows of same compound with different IC50 values. 
# count how many IC50 values exist per compound

compound_counts = df.groupby("molecule_chembl_id")["standard_value"].count() 
print("Number of IC50 measurements per compound (top 10):")
print(compound_counts.head(10), "\n")

# Plot IC50 distribution

plt.figure(figsize=(8,5))
plt.hist(df["standard_value"], bins=50, color='skyblue', edgecolor='black') 
plt.xlabel("IC50 (nM)") 
plt.ylabel("Number of Compounds") 
plt.title("ASK1 Compound IC50 Distribution") 
plt.tight_layout() 
plt.savefig("plots/ic50_hist.png", dpi=300)  
plt.show() 

# Save cleaned dataset
df.to_csv("ASK1_Dataset_cleaned.csv", index=False) #Saves my current dataframe to a CSV file, but dont save the row numbers as a separate column
print("Cleaned dataset saved as 'ASK1_Dataset_cleaned.csv'") # Confirms cleaned file saved successfully



