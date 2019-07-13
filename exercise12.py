import pizza_maker as toppings

def pizza_maker():
    print('How many pizzas do you want to order?')
    quantity_pizza = int(input())
    indiv_pizza = range(1,(quantity_pizza+1))
    print(yes_or_no(get_quantity(quantity_pizza)))
    for x in indiv_pizza:
        toppings.display_prices()
        print(f'How many toppings for pizza {x}?')
        num_toppings = int(input())
        print(f'You have ordered a pizza with {num_toppings} toppings')
        
def yes_or_no(input_val):
    # check if input value is yes
    if input_val == "yes":
        #run toppings function
        print(toppings.display_prices())
        return 'What toppings would you like?'
    elif input_val == "no":
        return quantity
    else:
        return "Something went wrong" 

def get_quantity(input_val):
    pizza_quantity.append(input_val)
    confirm = input(f'''You ordered {input_val} pizzas, Correct?
    enter \'yes\' or \'no\' \n''')
    return confirm
  

pizza_quantity = []
# quantity = input('How many pizzas do you want to order?\n')
# print(yes_or_no(get_quantity(quantity)))

pizza_maker()

# handle bulk orders of pizzas
# pizzas have various toppings on each
# ask the user for an input call it 'quantity'
# ask the user for quantity more numbers - toppings

# def new_pizza_order():
#     print("How many pizzas do you want to order?")
#     quantity = int(input())
#     pizzas = range(1, quantity + 1)
#     for each_pizza in pizzas:
#         print(f"How many toppings would you like on pizza {each_pizza}?")
#         topping_num = int(input())
#         string = f"You have put {topping_num} toppings on pizza {each_pizza}."
#         print(string)
#     return string

# print(new_pizza_order())




#### make topping selector next 
# continued in pizza_maker 
