import pizza_maker as toppings 

# print welcome to the pizza shop 
print('Welcome to Jay\'s pizza shop')
# print prices for sizes and toppings 

def show_all_prices(): 
    print("-----------MENU-----------")
    for key, value in toppings.sizes.items(): 
        string = f'\t{key}: {value}'
        print(string)
    print(toppings.line())
    return True

show_all_prices()
    # for size in toppings.pizza['sizes']
    #     size = toppings.pizza['size']['small']
# get user input for how many pizzas they want to order 

# ask the user what size pizza they want for every pizza 
# add size to pizza dictionary 

# show toppings 
# ask the user which toppings they want FOR EACH PIZZA 
    # add topping price to total for every item chosen 
    # if they choose meat add meat price total 
    # if they choose cheese add cheese price to total 
    # if they choose cheese add veggie price to total 

# print every pizza 