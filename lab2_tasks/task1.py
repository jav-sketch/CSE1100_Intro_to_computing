# This program collects user input for name, age, and city, then prints a formatted message.]\
def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    
    print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")

if __name__ == "__main__":
    main()