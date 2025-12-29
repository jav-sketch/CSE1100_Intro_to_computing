import random
ran_list = []
n = int(input("How many random numbers would you like to generate? "))
for i in range(n):
    num = random.randint(1,10)
    ran_list.append(num)
print(f"The generated list is: {ran_list}")

# Initialize count for each value in the list that is less than 5
count = 0
for val in ran_list:
    # print(f"value: {val}") 
    if val < 5:
        count += 1
print(f"value: {val}, count of values less than 5: {count}")
