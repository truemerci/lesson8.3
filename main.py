try:
    number = input("Enter the number: ")
    print(int(number))
except ValueError:
    print("Incorrect value")
