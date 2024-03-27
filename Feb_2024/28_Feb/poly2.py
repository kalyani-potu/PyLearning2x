class India:
    def capital(self):
        print("Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing country")

class USA:
    def capital(self):
        print("Washinton DC")

    def language(self):
        print("English")

    def type(self):
        print("Developed country")


obj_ind = India()
obj_us = USA()

for country in (obj_ind,obj_us):
    country.capital()
    country.language()
    country.type()