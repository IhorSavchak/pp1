inp = (input("Enter the 24-hour format time(hh.mm): "))
hours, minutes = map(int, inp.split('.'))
if hours <= 12:
    print(f"{inp}am")
else:
    format = hours - 12
    print(f"{format}.{minutes}pm")