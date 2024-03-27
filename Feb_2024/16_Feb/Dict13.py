api_response = {
    'first_name' : 'kalyani',
    'age' : 33,
    'last_name' : 'potu',
    'email' : 'kalyani.potu@gmail.com',
    'password' : 'Test@4321',
    'commission' : 10

}
print(api_response)
api_response['password']= 'kalyani@123'
print(api_response)
print(api_response.get('password'))

api_response.update({"commission":25})
print(api_response)