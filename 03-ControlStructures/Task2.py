number = int(input("Enter a number: "))
if number > 0:
    print("The number is already on its' absolute value")
if number < 0:
    total = number * -1
    print(f"|{number}| = {total}")