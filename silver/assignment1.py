import math 

shape = input("Type shape (s for square, r for rectangle, c for circle): ") 

if shape == "s":
    side = float(input("length: "))
    area = side ** 2

elif shape == "r":
    length, width = map(float, input("Type length and width separated by space: ").split())
    area = length * width
elif shape == "c":
    radius = float(input("radius: "))
    area = math.pi * radius ** 2
else:
    print("Invalid shape input. Please enter 's' for square, 'r' for rectangle, or 'c' for circle.")
    area = None 

if area is not None:
    print(f"The area is {area:.4f}")