class VWOLoginPage :
    email = None
    password = None

    def __init__(self, o_email, o_password):
        self.email = o_email
        self.password = o_password
    def loginconfirm(self):
        if self.password == "pass123" :
            print("You are allowed to enter")
        else :
            print("Invalid user")

kalyani = VWOLoginPage('kalyani.potu@gmail.com', 'password123')
kalyani.loginconfirm()

krithi = VWOLoginPage('krithi,p@gmail.com', 'pass123')
krithi.loginconfirm()

print(id(kalyani))
print(id(krithi))
