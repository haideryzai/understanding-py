# Create a list of cubes (e.g., x^3) for numbers 1–10.
# Create a list of numbers from 1–20 that are divisible by both 2 and 3.
# creating a 2D list using list comprehension

cubes = [x**3 for x in range(1,11)]

divisible_by2_and_3= [x for x in range(1,20) if x % 6 == 0]

matrix2D =  [[x for x in range(1, 100) if x % 6 == 0] for _ in range(1, 3)]

print("Cubes : ",cubes)
print(f"divisible_by2_and_3 : {divisible_by2_and_3}")
print("2D Matrix", matrix2D)