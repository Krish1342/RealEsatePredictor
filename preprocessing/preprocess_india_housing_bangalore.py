import pandas as pd

# Load dataset
file_path = r"datasets/india_housing_prices.csv"
df = pd.read_csv(file_path)

# Filter for Bangalore city
bangalore_df = df[df["City"].str.contains("Bangalore", case=False, na=False)]

# Drop duplicates
bangalore_df = bangalore_df.drop_duplicates()

# Handle missing values (drop rows with missing critical info)
bangalore_df = bangalore_df.dropna(subset=["Price", "City"])

# Save cleaned Bangalore housing data
bangalore_df.to_csv(
    r"c:\Users\drket\OneDrive\Desktop\Codes\RealEstate\datasets\bangalore_housing_prices_cleaned.csv",
    index=False,
)

print("Bangalore housing prices data cleaned and saved.")
