# Create a Student class that inherits from Person. 
# Add attributes like student_id and a method to display the student's details.

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age= age
        self.city = city

    def introduce(self):
        return f"Hi, I'm {self.name} from {self.city}, and I'm {self.age} years old."

class Student(Person):
    def __init__(self, name, age, city, student_id):
        super().__init__(name, age, city)
        self.student_id = student_id
        
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} My student ID is {self.student_id}."
    
student_object = Student("Haider", 23, "Karachi", "S12345")
result = student_object.introduce()

print(result)