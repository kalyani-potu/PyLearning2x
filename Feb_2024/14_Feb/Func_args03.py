def make_pizza(*toppings):
    for top in toppings:
        print(top)
    print('-----')
pizza1 = make_pizza('olives','onions')
pizza2 = make_pizza('tomatoes','chicken','onions')
pizza3 = make_pizza('mushroom','onions','corn','pineapple')
