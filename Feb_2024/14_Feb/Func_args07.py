def make_pizza_base(*toppings, base = "thin"):
    print(toppings, base)

    for topping in toppings:
        print(topping)


pizza1 = make_pizza_base('mushroom', 'onions', 'corn', 'pineapple') #base is taken default value
pizza2 = make_pizza_base('chicken', 'onions', 'corn', 'pineapple', base='wheat')
