inp1 = float(input("Enter your height in cm:"))
inp2 = int(input("Enter your weight in kg:"))
BMI = int(inp2/((inp1/100)**2))
print(BMI)
if BMI>=18.5 and BMI<=25:
    print("The weight is correct")