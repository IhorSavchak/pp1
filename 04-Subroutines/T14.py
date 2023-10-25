inp = int(input("Enter the amount in PLN: "))
zl5 = 0
zl2 = 0
zl1 = 0
while inp > 0:
    if inp > 5:
        zl5 += 1
        inp -= 5
    if inp > 2:
        zl2 += 1
        inp -= 2
    else:
        zl1 += 1
        inp -= 1
print(f"Minimum coins for {inp} PLN: ({zl5}) 5 PLN, ({zl2}) 2 PLN, ({zl1}) 1 PLN")
