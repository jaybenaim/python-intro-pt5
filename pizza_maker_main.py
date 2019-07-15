import pizza_maker as toppings 

# print welcome to the pizza shop 
print('Welcome to Jay\'s pizza shop')
# print prices for sizes and toppings 
def show_all_prices(): 
    print("-----------MENU-----------")
    # get the size with the price and print it 
    for size, price in toppings.sizes.items(): 
        #show the size and price 
        string = f'\t{size}: ${price}0'
        print(string)
    print(toppings.line())
    return True

show_all_prices()
# get user input for how many pizzas they want to order 
def get_number_of_pizzas():
    number_of_pizzas = input("How many pizzas would you like to order?\n") 
    return number_of_pizzas 

# ask the user what size pizza they want for every pizza 
def get_sizes(): 
    num = int(get_number_of_pizzas()) + 1
    ranged = range(1, num ) 
    for pizza in ranged: 
        sizes = input("How many toppings would you like to add to pizza {}".format(pizza))
        
    return sizes 

print(get_sizes()) 
# add size to pizza dictionary 

# show toppings 
# ask the user which toppings they want FOR EACH PIZZA 
    # add topping price to total for every item chosen 
    # if they choose meat add meat price total 
    # if they choose cheese add cheese price to total 
    # if they choose cheese add veggie price to total 

# print every pizza 