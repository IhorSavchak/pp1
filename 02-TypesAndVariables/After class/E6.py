inp = input("Enter the vehicle registration number: ")
real = inp[:2].upper() in ["KR", "KK"]
print(real)