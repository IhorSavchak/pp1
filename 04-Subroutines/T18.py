a = 15
b = 4
symbol = "*"
for i in range (a,b):
    if i == 0 or i == b - 1:
        print(str(symbol)* a)
    else:
        print(symbol + " " * b + symbol)