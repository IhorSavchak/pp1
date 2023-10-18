name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
age1 = int(input("Enter the age of the first person: "))
age2 = int(input("Enter the age of the second person: "))
if age1 > 18 and age2 > 18:
    print(f"Neither {name1} nor {name2} are underaged")
if age1 < 18 and age2 < 18:
    print(f"Both {name1} and {name2} are underaged")
else:
    print(f"Either {name1} or {name2} is underaged")