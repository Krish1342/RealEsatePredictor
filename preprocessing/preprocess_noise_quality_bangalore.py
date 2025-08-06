import pandas as pd

# Load dataset
file_path = (
    r"datasets/noise_quality.csv"
)
df = pd.read_csv(file_path)

# Filter for Bangalore city (if city column exists, else filter by location names)
if "City" in df.columns:
    bangalore_df = df[df["City"].str.contains("Bangalore", case=False, na=False)]
else:
    bangalore_df = df[df["Location"].str.contains("Bangalore", case=False, na=False)]

# Drop duplicates
bangalore_df = bangalore_df.drop_duplicates()

# Handle missing values (drop rows with missing critical info)
bangalore_df = bangalore_df.dropna(subset=["Location"])

# Save cleaned Bangalore noise quality data
bangalore_df.to_csv(
    r"c:\Users\drket\OneDrive\Desktop\Codes\RealEstate\datasets\bangalore_noise_quality_cleaned.csv",
    index=False,
)

print("Bangalore noise quality data cleaned and saved.")
