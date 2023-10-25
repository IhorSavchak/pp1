num = (input("Enter EAN-13 article number: "))
if num.isdigit() and len(num) == 13:
    print("The number is correct")
    if num[:3] == "590":
        print("The number is from Poland")
    else:
        print("The number isn't from Poland")
else:
    print("The number is invalid")