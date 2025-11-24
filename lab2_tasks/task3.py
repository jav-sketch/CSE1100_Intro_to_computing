# This programs generates two numbers randon numbers between 1 and 50 and prints their sum.
import random
# num1 = random.sample(range(1, 51), 1) # gererate a random number between 1 and 50
# num2 = random.sample(range(1, 51), 1) # gererate a random number between 1 and 50
# sum = num1[0] + num2[0]

def random_sum():
    set1 = random.sample(range(100, 200), 1) # gererate a random number between 100 and 200
    set2 = random.sample(range(100, 200), 1) # gererate a random number between 100 and 200
    # total = set1[0] + set2[0]
    # If the first number is greater than the second, return their sum
    if set1 > set2:
        result = set1[0] + set2[0]
        return result
    # If the second number is greater than the first, return their product
    elif set2 > set1:
        result = set2[0] * set1[0]
        return result
    # If both numbers are equal and their sum is greater than 125, return their average
    elif set1 and set2 > 125:
        result = (set1[0] + set2[0]) / 2
        return result
    # If either number is greater than or equal to 150, return the absolute difference between them
    elif set1 >= 150 or set2 >= 150:
        result = abs(set1[0] - set2[0])
        return result
    else:
        result = set1[0] + set2[0]
        return result

        
   
if __name__ == "__main__":
    result = random_sum()
    print(f"The sum of two random numbers is: {result}")
    
    print(f"The average of two random numbers is: {result}")
    print(f"The absolute difference of two random numbers is: {result}")
    print(f"The product of two random numbers is: {result}")