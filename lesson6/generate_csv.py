import pandas as pd
import random

# Generate student data
num_students = 500000  # Number of students
data = []

for i in range(num_students):
    marks = random.randint(30, 100)  # Random marks between 30 and 100
    # Assign grades based on marks
    if marks >= 90:
        grade = 1
    elif marks >= 80:
        grade = 2
    elif marks >= 70:
        grade = 3
    elif marks >= 60:
        grade = 4
    elif marks >= 50:
        grade = 5
    else:
        grade = 6
    
    data.append([i + 1, marks, grade])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Student_ID", "Marks", "Grade"])

# Save to CSV
df.to_csv("students_marks.csv", index=False)

print("CSV file 'students_marks.csv' has been created successfully!")
