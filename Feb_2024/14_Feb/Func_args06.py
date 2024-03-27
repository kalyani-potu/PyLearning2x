def make_pizza_base(*toppings, base):
    print(toppings, base)

    for topping in toppings:
        print(topping)


pizza1 = make_pizza_base('mushroom', 'onions', 'corn', 'pineapple') # error beacuse base is not passed
