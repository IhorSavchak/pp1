buy = float(input("Enter the Euro buying rate: "))
sell = float(input("Enter the Euro selling rate: "))
spread = sell - buy
final_res = "{:.4f}".format(spread)
print(f"The spread between buying and selling is: {final_res}")