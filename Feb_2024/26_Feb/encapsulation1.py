class Myclass:
    def __init__(self):
        self.name = 'kalyani'
        self.__priv_var = "ppppp"
    def public_fun(self):
        print("public function")
    def __private_func(self):
        print('This is private')
    def private_public(self): # accessing private function by using public function
        self.__private_func()
        print("private variable is ", self.__priv_var) # accessing private variable by using public function

obj_ref = Myclass()
obj_ref.public_fun()
obj_ref.private_public()
#print(obj_ref.__priv_var)