items = ["shoes", "underwear", "jacket"]
inp = input("Choose the product from a list (shoes, underwear, jacket): ")
addrinse = input("Allow rinse? (True/False): ")
addspin = input("Add a spin?(True/False): ")
if addrinse == "True":
    addrinse == True
else:
    addrinse == False
if addspin == "True":
    addspin == True
else:
    addspin == False
time = 0
if inp == "shoes":
    time += 20
if inp == "underwear":
    time += 70
if inp == "jacket":
    time += 40
if addrinse == True:
    time += 15
if addspin == True:
    time += 9
print(time)