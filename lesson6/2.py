import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, 'hpd.csv')
df = pd.read_csv(csv_file_path)

# Prepare the data
X = df[["Area", "Bedrooms"]]  # Input features (independent variables)
y = df["Price"]  # Target variable (dependent variable)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)


input_data = [{'Area': 1500, 'Bedrooms': 3}, {'Area': 2000, 'Bedrooms': 4 }, {'Area': 2500, 'Bedrooms': 5 }]

input_df = pd.DataFrame(input_data)

# Predict prices using the trained model
predictions = model.predict(input_df)

# Print the predicted prices
print("Predicted Prices:", predictions)