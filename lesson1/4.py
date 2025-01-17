# Use a for loop to display the multiplication table of a number entered by the user.


def display_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")



if __name__ == "__main__":
    number = int(input("Enter a number: "))
    display_table(number)