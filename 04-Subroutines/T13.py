deci = int(input("Write down a decimal number: "))
binary = ""
while deci > 0:
    binary = str(deci % 2) + binary
    deci //= 2
print(f"Binary Representation: {binary}")