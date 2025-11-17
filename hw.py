# Homework
print("Basic Python Calculator")
print("This collects and stores two numbers from a user. Adds them if the first number is larger than the second, and multiplies them otherwise.")
firt_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

# if firt_num > second_num:
#     result = firt_num + second_num
#     print(f"The sum of {firt_num} and {second_num} is: {result}")
# else:
#     result = firt_num * second_num
#     print(f"The product of {firt_num} and {second_num} is: {result}")
# Refactored code with function that adds or multiplies based on condition
def add_or_multiply(a, b):
    if a > b:
        return a + b
    else:
        return a * b

return_value = add_or_multiply(firt_num, second_num)
print(f"The result is: {return_value}")