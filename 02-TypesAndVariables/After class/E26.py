inp = input("Enter a four-digit binary number: ")

if len(inp) == 4 and inp.isdigit():
    decimal = 0

    for i in range(4):
        bit = int(inp[i])
        decimal = decimal * 2 + bit

    print("Decimal Number:", decimal)
else:
    print("Invalid input. Please enter a four-digit binary number.")