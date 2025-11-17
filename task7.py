print("This program performs addition, multiplication, and averaging of two numbers.")
# User input for two numbers and converting them to integers
num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))

# Function definitions
def add_numbers(a, b):
    return a + b
def multiply_numbers(a, b): 
    return a * b
def average_numbers(a, b):     
    return (a + b) / 2

# Function calls 
sum_result  = add_numbers(num_one, num_two)
product_result = multiply_numbers(num_one, num_two)
average_result = average_numbers(num_one, num_two)

# final output with f-string 
print("For the numbers", num_one, "and", num_two, ":\n" f"The sum is {sum_result}\n the product is {product_result}\n and the average is {average_result}.")