inp = int(input("Enter the price before: "))
inp1 = int(input("Enter the current price: "))
disc = (inp - inp1) / inp * 100
if disc >= 10:
    print("Buy the product!")
if disc < 10:
    print("The discount is incignificant")
print(f"{disc}%")