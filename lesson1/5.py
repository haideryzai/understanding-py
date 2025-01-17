# Take a string input from the user and:
# Print its length.
# Convert it to uppercase.
# Replace a specific word with another word.


def process_string(string):
    print("String's length: ", len(string))
    print("Uppercase: ", string.upper())
    replaced_string = string.replace("world", "world")
    print("Replaced string: ", replaced_string)
    

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    process_string(user_input)
    