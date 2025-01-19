# Create a function add_numbers that takes two numbers as input and returns their sum. Call it with different arguments.


def add_numbers(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    number1 = float(input("Enter first number : "))
    number2 = float(input("Enter second number : "))
    
    print(f"Sum : {add_numbers(num1=number1, num2=number2)}")
    