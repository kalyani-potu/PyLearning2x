api_response = {
    'first_name' : 'kalyani',
    'age' : 33,
    'last_name' : 'potu',
    'email' : 'kalyani.potu@gmail.com',
    'password' : 'Test@4321',
    'commission' : 10

}
print(api_response)
print(type(api_response))
print(api_response['age'])
print(api_response.get("password"))

for k,v in api_response.items():
    print(k, "-", v)