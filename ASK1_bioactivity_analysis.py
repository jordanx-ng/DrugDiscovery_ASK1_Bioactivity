import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
if not os.path.exists("plots"):   #create a plots folder if it doesnt exist
    os.makedirs("plots")


# ---------------------------
# STEP 1: Load the CSV
# ---------------------------
# lets print the first 5 rows of data and print all the column names so we know what we can work with

df = pd.read_csv("ASK1_Dataset.csv")
print("First 5 rows of dataset:")
print(df.head(), "\n")

print("Column names:")
print(list(df.columns), "\n")

# ---------------------------
# STEP 2: Clean IC50 values
# ---------------------------
# dropna(subset=[ ]) → removes rows where the IC50 value is missing.
# pd.to_numeric(   , errors="coerce") → converts IC50 to numbers (in this case it was text). Any non-number becomes NaN, then we drop NaNs again just in case
# This is because i learned that in drug discovery, you cant calculate or plot IC50 if the value is missing or in text

df = df.dropna(subset=["standard_value"])  # drop missing IC50
df["standard_value"] = pd.to_numeric(df["standard_value"], errors="coerce")
df = df.dropna(subset=["standard_value"])  # drop invalid IC50
print("Data cleaned. Number of valid rows:", len(df), "\n")    # this shows how many valid rows remains after cleaning

# ---------------------------
# STEP 3: Summary statistics
# ---------------------------
# describe() gives count, mean, std, min, max, quartiles of IC50 values
# I do this so it tells us how potent compounds are on average, and the range of potencies

print("Summary statistics for IC50 (nM):")
print(df["standard_value"].describe(), "\n")

# ---------------------------
# STEP 4: Mean IC50 per compound
# ---------------------------
# groupby("molecule_chembl_id") → groups data by unique compound IDs because in the dataframe, there are multiple rows of same compound with different IC50 values.
#["standard_value"].mean() → computes mean IC50 per compound.
# head(10) → shows top 10 compounds.
# I do this because i learned that compounds with low IC50 values are generally considered good inhibitors because they are highly potent

mean_ic50_per_compound = df.groupby("molecule_chembl_id")["standard_value"].mean()
print("✅ Mean IC50 per compound (top 10):")
print(mean_ic50_per_compound.head(10), "\n")  #just shows the first 10 compounds mean IC50 values for visualisation

# ---------------------------
# STEP 5: Count measurements per compound
# ---------------------------
# groups data by unique compound IDs because in the dataframe, there are multiple rows of same compound with different IC50 values. 
# count how many IC50 values exist per compound

compound_counts = df.groupby("molecule_chembl_id")["standard_value"].count() 
print("Number of IC50 measurements per compound (top 10):")
print(compound_counts.head(10), "\n")

# ---------------------------
# STEP 6: Plot IC50 distribution
# ---------------------------
# I made the width 8 inches and height 5 inches so the plot is large enough to see details

plt.figure(figsize=(8,5))
plt.hist(df["standard_value"], bins=50, color='skyblue', edgecolor='black') #makes a histogram plotting IC50 values, into 50 intervals (more detailed), outlined bars in black for clarity
plt.xlabel("IC50 (nM)") #x axis
plt.ylabel("Number of Compounds") #y axis
plt.title("ASK1 Compound IC50 Distribution") #Adds a title at the top of the plot
plt.tight_layout() #adjusts layout to prevent overlap
plt.savefig("plots/ic50_hist.png", dpi=300)  # save the plot image in plots/ folder
plt.show() #displays my plot when i run the script


# ---------------------------
# STEP 7: Save cleaned dataset
# ---------------------------
df.to_csv("ASK1_Dataset_cleaned.csv", index=False) #Saves my current dataframe to a CSV file, but dont save the row numbers as a separate column
print("Cleaned dataset saved as 'ASK1_Dataset_cleaned.csv'") # Confirms cleaned file saved successfully


