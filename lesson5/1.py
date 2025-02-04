# Create a Person class with attributes like name, age, and city.
# Add a method to introduce the person, e.g., "Hi, I'm Haider from Karachi, and I'm 25 years old."

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age= age
        self.city = city

    def introduce(self):
        return f"Hi, I'm {self.name} from {self.city}, and I'm {self.age} years old."
    

person_object = Person("Haider", 23, "Karachi")
result = person_object.introduce()

print(result)

