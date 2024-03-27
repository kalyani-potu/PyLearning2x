dict1 = {'a' :  1, 'bbb' : 2, 3 : 'cc' , 'd' : True, 4 : False, 5 : 'cc', 6 : 66, 6 : 'aa'}
print(len(dict1))
print(dict1) # if keys are duplicate, it takes the last assignment, length is calculated for only one key
print(dict1['bbb'])
print(dict1[4])

#dict2 = dict( a = 1, bbb = 2, 3 = 'cc') #This gives error, when dict function is called, keys are variables, variable names cannot be integers
dict2 = dict(a = "John", bbb = 36, c = "Norway")
print(dict2)
print(dict2['bbb'])
print(dict2['c'])