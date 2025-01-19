# Create a program that:
# Checks if a file named log.txt exists.
# If it doesn’t exist, creates it and writes "Log created."
# If it exists, appends "Log updated." and the current timestamp to it.

import os

if not os.path.exists("log.txt"):
    with open("log.txt", "w") as file:
        file.write("Log created.")
else:
    with open("log.txt", 'a') as file:
        file.write("\n Log updated")
