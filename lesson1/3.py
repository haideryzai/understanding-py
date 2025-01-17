# Write a program to check if a user is a minor or an adult based on their input age.

def check_age(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"

age = int(input("Enter your age: "))


if __name__ == "__main__":
    result = check_age(age)
    print(f"You are a {result}.")