# Create a loop that prints the multiplication table (1–10) for a given number.
# Use enumerate() to iterate through a list of colors and print the index with each color.


if __name__ == "__main__":
    number = int(input("Enter number : "))
    
    # 1
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")
    
    # 2
    
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
    
    for index, color in enumerate(colors):
        print(f"{index} : {color}")