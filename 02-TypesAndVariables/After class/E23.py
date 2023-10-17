inp = float(input("Enter price: "))
inp2 = float(input("Enter discount: "))
convertion = 1 - inp2 / 100
final_price = inp * convertion
reduction = inp - final_price
print("The product is ", reduction ,"cheaper")
print("The final price is:", final_price)