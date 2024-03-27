class SecureClass:
    heading = "VMOLogin"

  
    def __init__(self):
        self.browser = "chrome"
    def submit(self):
        self.__password = "pass123"
        self.username = "admin"

obj = SecureClass()
print(obj.heading)
print(obj.browser)
print(obj.username) #giving error
#obj.submit()
#print(obj.username) # after calling submit(), this is not giving error
