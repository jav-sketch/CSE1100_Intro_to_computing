#This program generates n rand between 1 and 10 and ave them to a list and prints the list
import random
def generate_random_list(n):
    list_of_randoms = []
    for rand_num in range(10):
        rand_num = random.randint(1, 10)
        list_of_randoms.append(rand_num)
    return list_of_randoms

#Determines how many of the numbers in the list are less than 5
def count_less_than_five(list_of_randoms):
    count = 0
    for num in list_of_randoms:
        if num < 5:
            count += 1
    return count

#Determines the largetst and smallest number in the list
def largest_and_smallest(list_of_randoms):
    largest = max(list_of_randoms)
    smallest = min(list_of_randoms)
    return largest, smallest

# 
if __name__ == "__main__":
    n = 10
    random_list = generate_random_list(n)
    count = count_less_than_five(random_list)
    largest, smallest = largest_and_smallest(random_list)
    print(f"List of {n} random numbers between 1 and 10: {random_list}")
    print(f"Count of numbers less than 5: {count}")
    print(f"Largest number: {largest}"f"\nSmallest number: {smallest}")
