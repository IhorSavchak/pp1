
pin = "0805"
attempts = 0
while attempts < 3:
    inp = int(input("Try to guess the 4-digit pincode: "))
    if inp == pin:
        print("The pin is correct")
    else:
        print("Incorrect")
        attempts =+1
        if attempts > 3:
            print("The card has been blocked")