# Write a program to:
# Create a file named data.txt.
# Write a few lines of text into the file.
# Read and print the content of the file.

def createFile():
    with open("./data.txt", "w") as file:
        file.write("Hello g, how are you doin?")


def readFile():
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
    
    
if __name__ == "__main__":
    createFile()
    readFile()