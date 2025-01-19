# Create a function process_numbers(*args) that:
# Accepts any number of arguments.
# Returns the sum and the average of the numbers.

def process_numbers(*args):
    sum = 0
    for n in args:
        sum = sum+int(n)
        
    avg = sum / len(args)
    
    return {"sum": sum, "avg": avg}
   
    
if __name__ == "__main__":
    print(process_numbers(23, 37, 87))