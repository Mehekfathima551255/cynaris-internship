
import pandas as pd
from pathlib import Path

# Create reports folder
Path("reports").mkdir(exist_ok=True)

# 1. Load the dataset
df = pd.read_csv("data/district_literacy.csv")

print("INITIAL DATA")
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# 2. Inspect dataset
print("\nDATA INFORMATION")
df.info()

print("\nSTATISTICS")
print(df.describe())

# 3. Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 4. Check duplicate rows
print("\nDUPLICATES:", df.duplicated().sum())

# 5. Clean column names
df.columns = df.columns.str.strip()

# 6. Remove duplicate rows
df = df.drop_duplicates()

# 7. Handle missing values
df = df.dropna(subset=["District", "State", "Literacy"])

# 8. Clean percentage column
df["Growth"] = pd.to_numeric(
    df["Growth"].astype(str).str.replace("%", "", regex=False),
    errors="coerce"
)

# 9. Save cleaned dataset
df.to_csv("reports/cleaned_literacy.csv", index=False)

# 10. Display final results
print("\nCLEANED DATA")
print("Final shape:", df.shape)
print(df.head())
print("\nCleaning completed successfully!")
