import pandas as pd
import numpy as np
import os

# Create a DataFrame manually with columns "Name", "Age", and "Salary", and add at least 5 people.
data = {
    'Name': ['Aman', 'Poonam', 'Bobby', 'Alison', 'Annie'],
    'Age': [28, 24, 32, 55, 54],
    'Salary': [100000, 120000, 20000, 45000, 78000]
}


df = pd.DataFrame(data)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, 'data.csv')

df.to_csv(csv_file_path, index=False)
print("Created csv file successfully.")

# Filter and show only people who have a salary greater than 40,000.
filtered_data = df[df['Salary'] > 40000]
print(f"People who have a salary greater than 40,000:\n{filtered_data}")

# Add a new column "Experience" with random values (for example, years of experience)
np.random.seed(0)
df['Experience'] = np.random.randint(1, 21, size=len(df))

# Save the updated DataFrame to a new CSV file
updated_csv_file_path = os.path.join(script_dir, 'updated_data.csv')
df.to_csv(updated_csv_file_path, index=False)

# new column "Experience" with random values (for example, years of experience)
print(f"Experience with random values (for example, years of experience) \n {df}")