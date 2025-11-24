# This program collects user input for name, age, and city, then prints a formatted message.]\
def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    # phone number input as an additional feature
    phone = int(input("Enter your phone number: "))
    # Convert age to integer
    age = int(age)
    # Print the formatted message with all collected information
    print(f"Hello, my name is {name}. I am {age} years old and I live in {city} and my phone number is {phone}.")

if __name__ == "__main__":
    main()