def pizza_maker():
    print('How many pizzas do you want to order?')
    quantity_pizza = int(input())
    # order_num = toppings.pizza_order_num()
    # toppings.pizza_order_num
    ind_pizza = range(1,(quantity_pizza+1))

    print(ind_pizza)
print(pizza_maker())