def say_hello():
    print("Hello")


say_hello()

result = say_hello()
print(result) # None because say_hello is not returning anything

def hello_name(name):
    print("hello ", name)

hello_name('kalyani')

def func1(name='DefaultName'):
    print("hello ", name)

func1() # takes default value that it passed during function definition
func1('Drithi - Krithi')

def func2(name,age):
    print("Name is ", name , "Age is ",age)

func2('kalyani', 32)
