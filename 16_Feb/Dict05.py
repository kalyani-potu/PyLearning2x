k_details = dict(name='kalyani', age=32, isMale=False, Add= "WGL")
k_details2 = {'name' : 'kalyani', 90 : 34.4, "20" : 10, 'isFemale' : True}
print(k_details)
print(k_details.get('age'))
print(k_details.get('name'))
print(k_details['name'])

print(k_details2)
print(k_details2.get('90'))
print(k_details2[90]) #we can access directly or using get()
print(k_details2.get(90))
print(k_details2.get(20))
print(k_details2.get('20'))
print(k_details2.get('aaa'))

