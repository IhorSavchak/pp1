x = int(input("Write down the x coordinate: "))
y = int(input("Write down the y coordinate: "))
if x > 0 and y > 0:
    print("First quarter")
if x < 0 and y > 0:
    print("Second quarter")
if x < 0 and y < 0:
    print("Third quarter")
if x > 0 and y < 0:
    print("Fourth quarter")
if x == 0 and y == 0:
    print("The point is 0;0")