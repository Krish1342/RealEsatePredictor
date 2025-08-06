import pandas as pd

# Load Bangalore-specific dataset
file_path = r"datasets/Bangalore.csv"
df = pd.read_csv(file_path)

# Drop duplicates
df = df.drop_duplicates()

# Handle missing values (drop rows with missing critical info)
df = df.dropna(subset=["Price", "Location", "Total_Area"])

# Additional cleaning: remove rows with non-numeric price or area if needed
df = df[pd.to_numeric(df["Price"], errors="coerce").notnull()]
df = df[pd.to_numeric(df["Total_Area"], errors="coerce").notnull()]

# Save cleaned Bangalore data
df.to_csv(
    r"c:\Users\drket\OneDrive\Desktop\Codes\RealEstate\datasets\bangalore_real_estate_cleaned.csv",
    index=False,
)

print("Bangalore real estate data cleaned and saved.")
