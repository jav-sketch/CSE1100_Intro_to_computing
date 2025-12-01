#this program collects 10 numbers from the user and  prints them out one by one

#the program collects n values from the user and stores them in a list. The user determines n 
print("this program collects n values from the user and stores them in a list")



# print("Please enter 10 numbers:")
# def collect_and_print_numbers():
#     num_list = []
#     for i in range(10):
#         num = int(input(f"Enter number {i+1}: "))
#         num_list.append(num)    
#     print("You entered the following numbers:")
#     for number in num_list:
#         print(number)


# Prompts the use for the number of values to be collected
n = int(input("How many numbers would you like to enter? "))
#Fucntion that collects n numbers from the user and prints them one by one
def collectPrintNumbers(n):
    vals = []
    #for loop to collect n numbers
    for i in range(n):
        #val to store each number
        val = int(input(f"Enter number {i+1}: "))
        #appends/adds each number to the list
        vals.append(val)
    return vals

#calls the function and stores the returned list in numbers
numbers = collectPrintNumbers(n)
print(f"You entered the following list {numbers}:")
#prints the first and last elements of the list
print(f"The first number is: {numbers[0]}")
print(f"The last number is: {numbers[-1]}")