import pizza_maker as toppings

def pizza_maker():
    print('How many pizzas do you want to order?\n')
    quantity_pizza = input()
    # order_num = toppings.pizza_order_num()
    # toppings.pizza_order_num
    pizzas = int(quantity_pizza)
    pizzas_ordered = []

    for every_pizza in pizzas: 
        pizzas_ordered.append(every_pizza)
    # ind_pizza = range(1,(quantity_pizza+1))
    print(yes_or_no(get_quantity(quantity_pizza)))
    for each_pizza in pizzas_ordered:
        display_prices()
        print(f'How many toppings for pizza {each_pizza}?') # add this for toppings 
        num_toppings = int(input()) ### repitiotion error here somehere 
        print(f'You have ordered a pizza with {num_toppings} toppings to pizza {each_pizza} ')
        
def yes_or_no(input_val):
    # check if input value is yes
    if input_val == "yes":
        # run toppings function  
        return display_prices()
    elif input_val == "no":
        return pizza_maker()
    else:
        return pizza_maker() 

def get_quantity(input_val):
    pizza_quantity.append(input_val)
    confirm = input(f'''You ordered {input_val} pizzas, Correct?
    enter \'yes\' or \'no\' \n''')
    return confirm
  
def display_all_toppings(): 
    for topping, price in toppings.toppings.items():
        print(toppings.line_break) 
        print(f"{topping}: ${price}0")

def display_prices(): 
    total = 0
    display_all_toppings()
    for topping, price in toppings.toppings.items(): 
        print(toppings.line_break)
        print(f"{topping}: ${price}0")
        print(toppings.line_break)
        selected_toppings = f"How many {topping} toppings would you like to add to this pizza.  \n"
        selected_toppings = input(selected_toppings)
        # total calculator 
        counter = 0 
        while counter > int(selected_toppings): 
            total += toppings.toppings['meat']
            counter += 1 
            if counter == selected_toppings: 
                break 
            else: 
                counter += 1 
                print(total)

    print(price) 
pizza_quantity = []
pizza_maker()
# quantity = input('How many pizzas do you want to order?\n')
# print(yes_or_no(get_quantity(quantity)))



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
