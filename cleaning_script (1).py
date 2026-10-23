
import pandas as pd

# Load original dataset
file_path = "ApexPlanet_DataAnalytics_Dataset.xlsx"
df = pd.read_excel(file_path, sheet_name="Sales_Dataset")

# Convert order date to datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")

# Validate sales calculations
incorrect_sales = (
    df["Total_Sales"].round(2)
    != (df["Quantity"] * df["Unit_Price"]).round(2)
).sum()

# Report data quality
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Incorrect sales calculations:", incorrect_sales)

# Save cleaned dataset
df.to_csv("cleaned_sales_dataset.csv", index=False)
