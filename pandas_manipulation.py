
import pandas as pd
from pathlib import Path

# Create output folder
Path("reports").mkdir(exist_ok=True)

# 1. Load two real Indian Census datasets
literacy_df = pd.read_csv("data/district_literacy.csv")
population_df = pd.read_csv("data/district_population.csv")

# Clean numeric columns containing commas and percentage symbols
population_df["Population"] = pd.to_numeric(
    population_df["Population"].astype(str).str.replace(",", ""),
    errors="coerce"
)

population_df["Area_km2"] = pd.to_numeric(
    population_df["Area_km2"].astype(str).str.replace(",", ""),
    errors="coerce"
)

literacy_df["Growth"] = pd.to_numeric(
    literacy_df["Growth"].astype(str).str.replace("%", ""),
    errors="coerce"
)

# 2. Print dataset information
print("\n--- DATASET INFORMATION ---")
print("Literacy Dataset Shape:", literacy_df.shape)
print("\nData Types:\n", literacy_df.dtypes)
print("\nFirst 10 Rows:\n", literacy_df.head(10))

# 3. FILTER: Select districts with literacy above 80%
filtered_df = literacy_df[literacy_df["Literacy"] >= 80]

print("\n--- FILTER OPERATION ---")
print(filtered_df.head())

# 4. GROUPBY: Calculate average literacy for each state
grouped_df = literacy_df.groupby("State")["Literacy"].mean()

print("\n--- GROUPBY OPERATION ---")
print(grouped_df)

# 5. MERGE: Combine both datasets using District and State
merged_df = pd.merge(
    literacy_df,
    population_df,
    on=["District", "State"],
    how="inner"
)

print("\n--- MERGE OPERATION ---")
print("Merged Dataset Shape:", merged_df.shape)
print(merged_df.head())

# 6. PIVOT TABLE: Calculate total population for each state
pivot_df = pd.pivot_table(
    merged_df,
    index="State",
    values="Population",
    aggfunc="sum"
)

print("\n--- PIVOT TABLE ---")
print(pivot_df)

# 7. Clean the merged DataFrame
cleaned_df = merged_df.dropna(
    subset=["District", "State", "Literacy", "Population"]
)

# 8. Export cleaned DataFrame to CSV
csv_path = Path("reports/cleaned_indian_census.csv")
cleaned_df.to_csv(csv_path, index=False)

# 9. Export cleaned DataFrame to Parquet
parquet_path = Path("reports/cleaned_indian_census.parquet")
cleaned_df.to_parquet(parquet_path, index=False)

# 10. Compare CSV and Parquet file sizes
csv_size = csv_path.stat().st_size
parquet_size = parquet_path.stat().st_size

print("\n--- FILE SIZE COMPARISON ---")
print(f"CSV File Size: {csv_size:,} bytes")
print(f"Parquet File Size: {parquet_size:,} bytes")

print("\n--- FINAL SUMMARY ---")
print("Original Literacy Rows:", len(literacy_df))
print("Merged Rows:", len(merged_df))
print("Cleaned Rows:", len(cleaned_df))
print("CSV and Parquet exports completed successfully!")
