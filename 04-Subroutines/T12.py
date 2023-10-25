a = input("Are you interested in computer science? (Y/N): ") 
b =input("Do you like playing computer games? (Y/N): ")
c = input("Do you have an Instagram account? (Y/N): ")
if a == "Y":
    cs = "Yes"
else:
    cs = "No"
if b == "Y":
    cg = "Yes"
else:
    cg = "No"
if c == "Y":
    ia = "Yes"
else:
    ia = "No"
print(f"computer science {cs}")
print(f"computer game {cg}")
print(f"Instagram account {ia}")