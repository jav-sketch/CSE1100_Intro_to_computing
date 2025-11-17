#The user name function
def user_name():
    #User input for name
    print("Hello! Welcome to the program.")
    user_name = input("Enter your name: ")
    return user_name

def age():
    #User input for age
    user_age = input("Enter your age: ")
    return user_age

def height():
    #User input for height
    user_height = input("Enter your height in cm: ")
    return user_height

#Final output using an f-string and calling the functions
print(f"Hello, {user_name()}!, you are {age()} years old and {height()} cm tall.")
