print("Welcome to the interactive personal data collector!")
name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
height = float(input("Please enter your height in meters : "))
number = int(input("Please enter your favourite number : "))
print("\n Thank you! Here is the information we collected:\n")


print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Number: {number} (Type: {type(number)}, Memory Address: {id(number)})")

print(f"\nYour birth year is approximately: 1998 (based on your age of {age})")
print("\nThank you for using the Personal Data Collector. Goodbye!")
