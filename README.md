# ASK1 Bioactivity Mini-Project

## Overview
This mini-project analyzes the bioactivity of ASK1-targeting compounds from ChEMBL. Using IC50 data, the project computes mean potency per compound, evaluates measurement reliability, and visualizes the distribution of compound activities. IC50 values are also converted to pIC50 to standardize comparisons.

**Skills demonstrated:**  
- Data cleaning and preprocessing using pandas  
- Grouping, aggregation, and statistical summary  
- Visualization using matplotlib  
- Basic bioactivity interpretation for drug discovery  

---

## Dataset
- **Original dataset:** `ASK1_Dataset.csv`  
- **Cleaned dataset:** `ASK1_Dataset_cleaned.csv`  
- **Key columns:**
  - `molecule_chembl_id` — unique compound identifier  
  - `canonical_smiles` — compound chemical structure  
  - `standard_value` — IC50 (nM)  
  - `pIC50` — calculated log-transformed potency  
  - Physicochemical descriptors: MW, LogP, HBD, HBA, TPSA, RotB, Label  

**Source:** ChEMBL bioactivity database (public dataset)

---

## Workflow
1. **Load dataset** with `pandas.read_csv()`  
2. **Clean IC50 values**: remove missing or invalid entries and convert to numeric  
3. **Compute mean IC50 per compound** (`groupby()` + `mean`)  
4. **Count number of IC50 measurements per compound** to assess reliability  
5. **Visualize IC50 and pIC50 distributions** using matplotlib histograms  
6. **Save cleaned dataset** for downstream analysis  

---

## Key Findings
- Most compounds show IC50 values in the **range of 10 nM to 100,000 nM**  
- Compounds with multiple IC50 measurements are **more reliable for potency evaluation**  

---

## Example Plots

### IC50 Distribution
![IC50 Distribution](plots/ic50_hist.png)  
**Interpretation:** The majority of compounds cluster between 100 nM and 10,000 nM. A few highly potent compounds are visible in the lower IC50 range.

---

## How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/DrugDiscovery_ASK1_Bioactivity.git
