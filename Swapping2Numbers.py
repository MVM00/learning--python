# Swapping two numbers using the temp variable
num1 = input("Enter number1 before swapping: ")
num2 = input("Enter number2 before swapping: ")

# Convert input to integers
num1 = int(num1)
num2 = int(num2)
# Swapping Logic
temp = num1
num1 = num2
num2 = temp

print("Number1 after swapping" , num1)
print("Number2 after swapping", num2)

# Swapping two numbers without using temp variable

num1 = input("Enter number1 before swapping: ")
num2 = input("Enter number2 before swapping: ")
# Convert input to integers
num1 = int(num1)
num2 = int(num2)
# Swapping Logic
num1, num2 = num2, num1

print("Number1 after swapping" , num1)
print("Number2 after swapping", num2)






