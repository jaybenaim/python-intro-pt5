# # handle bulk orders of pizzas
# # pizzas have various toppings on each 
# # ask the user for an input call it 'quantity'
# # ask the user for quantity more numbers - toppings 

# def yes_or_no(input_val): 
#     # check if input value is yes 
#     if input_val == "yes": 
#         return 'What toppings would you like?'
#         #run toppings function 
#     elif input_val == "no":
#         return quantity
    
# def get_quantity(input_val):   
#     pizza_quantity.append(input_val)  
#     # print(int(input_val))
#     # while counter > int(input_val): 
#     #     counter += 1 
#     confirm = input(f"You ordered {input_val} pizzas, Correct?\n")
#     return confirm 
#     # return yes_or_no(confirm)
#     #     counter += 1 
#     #     confirm = f"You ordered {input_val} pizzas, yes or no?\n"
#     #     return confirm


# pizza_quantity = []
# quantity = input('How many pizzas do you want to order?\n')
# # print(get_quantity(quantity))
# # print(pizza_quantity)
# print(yes_or_no(get_quantity(quantity))) 

# def pizza_maker():
#     print('How man pizzas do you want to order?')
#     quantity_pizza = int(input())
#     indiv_pizza = range(1,(quantity_pizza+1))
#     for x in indiv_pizza:
#         print(f'How many toppings for pizza {x}?')
#         num_toppings = int(input())
#         print(f'You have ordered a pizza with {num_toppings} toppings')

# pizza_maker()


def new_pizza_order(): 
    print("How many pizzas do you want to order?")
    quantity = int(input())
    pizzas = range(1,quantity + 1)
    for each_pizza in pizzas: 
        print(f"How many toppings would you like on pizza {each_pizza}?")
        topping_num = int(input())
        string = f'You have put {topping_num} toppings on pizza {each_pizza}.'
        print(string)
    return string 
    

print(new_pizza_order()) 