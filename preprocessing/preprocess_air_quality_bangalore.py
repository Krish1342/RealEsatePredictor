import pandas as pd

# Load dataset
file_path = r"datasets/air_quality.csv"
df = pd.read_csv(file_path)

# Standardize column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Filter for Bangalore city
bangalore_df = df[df["city"].str.contains("bangalore", case=False, na=False)]

# Drop duplicates
bangalore_df = bangalore_df.drop_duplicates()

# Convert AQI to numeric and remove invalid values
bangalore_df["aqi"] = pd.to_numeric(bangalore_df["aqi"], errors="coerce")
bangalore_df = bangalore_df.dropna(subset=["aqi", "city"])

# Remove outliers (optional: AQI should be within a reasonable range)
bangalore_df = bangalore_df[(bangalore_df["aqi"] > 0) & (bangalore_df["aqi"] < 1000)]

# Reset index
bangalore_df = bangalore_df.reset_index(drop=True)

# Save cleaned Bangalore air quality data
bangalore_df.to_csv(
    r"c:\Users\drket\OneDrive\Desktop\Codes\RealEstate\datasets\bangalore_air_quality_cleaned.csv",
    index=False,
)

print("Bangalore air quality data cleaned and saved.")
