inp = int(input("Enter the first number: "))
inp2 = int(input("Enter the second number: "))
if inp or inp2 > 0:
    print(f"At least one of entered numbers {inp} and {inp2} is not negative")
else:
    print(f"At least one of entered numbers {inp} and {inp2} is negative")