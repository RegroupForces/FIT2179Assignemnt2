import pandas as pd

# Load the CSV
df = pd.read_csv(r"Data\a4ef8f10-5504-4bed-a8c0-950d4bcf53b5_Data.csv")

# Group by the "type" column
grouped = df.groupby("Series Name")

# Save each group as its own CSV
for group_name, group_df in grouped:
    filename = f"{group_name}.csv"
    group_df.to_csv(filename, index=False)

    print(f"Saved: {filename}")