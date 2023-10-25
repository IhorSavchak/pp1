num = int(input("Enter the number of products: "))
price = int(input("Enter a product price: "))
if num > 2:
    disc = 0.25 * (num - 2) * price
else:
    disc = 0
full_price = price * num
total = full_price - disc
print(f"Amount to pay: {total}")