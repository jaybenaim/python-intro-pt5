# handle bulk orders of pizzas
# pizzas have various toppings on each 
# ask the user for an input call it 'quantity'
# ask the user for quantity more numbers - toppings 

def yes_or_no(input_val): 
    # check if input value is yes 
    if input_val == "yes": 
        return 'What toppings would you like?'
        #run toppings function 
    elif input_val == "no":
        return quantity
    
def get_quantity(input_val):   
    pizza_quantity.append(input_val)  
    # print(int(input_val))
    # while counter > int(input_val): 
    #     counter += 1 
    confirm = input(f"You ordered {input_val} pizzas, Correct?\n")
    return confirm 
    # return yes_or_no(confirm)
    #     counter += 1 
    #     confirm = f"You ordered {input_val} pizzas, yes or no?\n"
    #     return confirm


pizza_quantity = []
quantity = input('How many pizzas do you want to order?\n')
# print(get_quantity(quantity))
# print(pizza_quantity)
print(yes_or_no(get_quantity(quantity))) 