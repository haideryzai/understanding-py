import os
import math
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_dir, 'students_marks.csv')
df = pd.read_csv(csv_file_path)

X= df[["Marks"]]
Y= df["Grade"]

grades= ["", "A+", "A", "B", "C", "D", "F"]

X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

input_data= [{"Marks": 98}]
input_df = pd.DataFrame(input_data)

predictions = model.predict(input_df)
grade_number= math.ceil(int(predictions[0]))

print(f"Prediction: {grade_number} {grades[grade_number]}")