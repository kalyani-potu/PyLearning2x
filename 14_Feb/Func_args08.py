def make_pizza_base(*toppings, base = "thin"):
    print(toppings, base)

    for topping in toppings:
        print(topping)
    return toppings, base


pizza_ar, pizza_b = make_pizza_base('chicken', 'onions', 'corn', 'pineapple', base='wheat')
print(pizza_ar)
print(pizza_b)