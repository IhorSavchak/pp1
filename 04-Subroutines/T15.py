for number in range(1, 31):
    final = ""
    
    if number % 3 == 0 and number < 30:
        final += 'THREE'

    if number % 5 == 0 and number < 30:
        final += 'FIVE'
        
    if number % 3 == 0 and number % 5 == 0:
        print("BINGO")
        
    if not final and number < 30:
        final = int(number)

    print(final)