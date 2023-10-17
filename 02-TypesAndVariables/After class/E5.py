a =int(input("Enter a:"))
b =int(input("Enter b:"))
c =int(input("Enter c:"))
x = (a + b + c)/2
y = int((x * (x - a) * (x - b) * (x - c))**0.5)
print("triangle area: ", x)
print("triangle circumference: ", y)
