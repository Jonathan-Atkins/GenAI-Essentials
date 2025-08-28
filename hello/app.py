import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

# Turn the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df, "\n")

# Select a column
print("Ages:\n", df["Age"], "\n")

# Filter rows
print("People over 30:\n", df[df["Age"] > 30], "\n")

# Get summary statistics
print("Summary statistics:\n", df.describe())