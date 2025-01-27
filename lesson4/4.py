# Write a lambda function to check if a string starts with the letter "a."
# Use filter() to find all strings starting with "a" in a list of words.

# 1

lambdaFunctionToCheckIfAwordStartsWithLetterA = lambda x : x.startswith("a")

print("lambdaFunctionToCheckIfAwordStartsWithLetterA", lambdaFunctionToCheckIfAwordStartsWithLetterA("Human"))
    
# 2
wordsList = ["alians", "animals", "humans"]

filteredWords = list(filter(lambda x: x.startswith("a"), wordsList))
print(f"Filtered Result : {filteredWords}")