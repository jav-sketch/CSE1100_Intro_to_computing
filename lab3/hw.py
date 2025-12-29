# This program generates and store a list of  50 values between 0 and 100.
# It reports the number of values 0-39, 40-49, 50-64, 65-74, 75-100
import random
lst = []
for val in range(0, 50):
    num = random.randint(0,100)
    lst.append(num)
print(f"The generated list is: {lst}")
# Initialize counters for each range
# counter
count = 0
# Count the number of values in each range
for num in lst:
    if 0 <= num and num <= 39:
        count += 1
        print(f"Number of values between 0-39: {count}")
    elif 40 <= num and num <= 49:
        count += 1
        print(f"Number of values between 40-49: {count}")
    elif 50 <= num and num <= 64:
        count += 1
        print(f"Number of values between 50-64: {count}")
    elif 65 <= num and num <= 74:
        count += 1
        print(f"Number of values between 65-74: {count}")
    elif 75 <= num and num <= 100:
        count += 1
        print(f"Number of values between 75-100: {count}")