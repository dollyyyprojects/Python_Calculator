# Python Developer Internship
# Task 1 : Calculator CLI App

# 1. Addition Function
def add(a, b):
  return a + b

# 2. Subtraction Function
def subtract(a, b):
  return a - b

# 3. Multiplication Function
def multiply(a, b):
  return a * b

# 4. Division Function
def divide(a, b):
  if b == 0:
    return "Cannot divide by zero"
  return a / b

#Main Program
while True:

      print("\n===== PYTHON CALCULATOR===")
      print("1. Addition")
      print("2. Subtraction")
      print("3. Multiplication")
      print("4. Division")
      print("5. Exit")

      choice = input("Enter your choice: ")

      if choice == "5":
        print("Thank you for using Calculator!")
        break

      if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

      try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        elif choice == "4":
            result = divide(num1, num2)

        print("Result:", result)

      except ValueError:
          print("Please enter valid numbers.")
