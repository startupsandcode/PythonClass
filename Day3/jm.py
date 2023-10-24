import pandas as pd
import random
import string

# Load the "metrics.csv" file
input_file = "MonthlyStoreMetrics.csv"
output_file = "results.csv"

# Load the CSV into a DataFrame
df = pd.read_csv(input_file)

# Generate random strings for the first column
random_strings = [''.join(random.choice(string.ascii_letters) 
                          for _ in range(10)) 
                            for _ in range(len(df))]

# Update the first column with the generated random strings
df.iloc[:, 0] = random_strings

# Save the modified DataFrame to "results.csv"
df.to_csv(output_file, index=False)

print(f"Modified data saved to {output_file}")

