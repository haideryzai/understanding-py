# Write a program that takes two inputs from the user (numerator and denominator)
# and handles any division errors (e.g., dividing by zero or invalid input).

def dividor():
    numerator = float(input("Enter numerator : "))
    denominator = float(input("Enter denominator : "))
    
    try:
        result = numerator/denominator
        print(f"Result : {result}")
    except ValueError:
        print("Division Error", ValueError)
        
if __name__ == "__main__":
    dividor()