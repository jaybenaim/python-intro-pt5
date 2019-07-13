one_to_hundred = range(100) 


#loop over numbers 1 to 100 
for number in one_to_hundred: 
    if number % 3 == 0 and number % 5 == 0:
        is_diveded_by_both = "BitMaker"
        print(is_diveded_by_both)
    elif number % 3 == 0: 
        is_diveded_by_3 = 'Bit'
        print(is_diveded_by_3)
    elif number % 5 == 0: 
        is_diveded_by_5 = 'Maker'
        print(is_diveded_by_5)
    else: 
        print(number)

