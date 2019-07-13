# import exercise12 as pizza_maker
line_break = "-------------------------------------------------------"
# a = pizza_maker.topping[0]
# print(a)
# print(new_pizza_order())

toppings = { 
    'meat': 0.50,
    'cheese': 1.00,
    'veggie': 0.35
}
meat = [ 
    'bacon', 
    'pepperoni', 
    'sausage',
    'chicken', 
    'proscuito' 
]
cheese = [ 
    'feta', 
    'mozz', 
    'extra' 
]
veggie = [
    'pineapple', 
    'pepper', 
    'olive', 
    'mushroom'
] 


# # or 
# all_toppings = 0.50 
# topping = [
#     'pepperoni',
#     'olives'
# ]

def display_prices(): 
    for topping, price in toppings.items():
        
        print(f"{topping}: {price}")


# display_prices()
# print(toppings['meat'])