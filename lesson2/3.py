# Create a dictionary with your name, age, and profession.
# Add a new key for your city.
# Print all keys and values using a loop.


me = { "name": "Haider", "age": 22, "profession": "Web Dev"}

me["city"] = "Swabi"

if __name__ == "__main__":
    for key, value in me.items():
        print(f"{key} : {value}")