import random


inp = int(input("Guess the number from 1 to 6: "))
a = random.randint(1, 6)
guessed = inp == a
print(guessed)