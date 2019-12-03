
# Nested function

def hello(name ="baron"):
    print("Hello called")
    def greet():
        return "Greeting called"
    def bye():
        return "Bye called"
    
    if name == "baron":
        return greet
    else:
        return bye
    
x = hello()
#print(x())

# Function as argument

def helloThere():
    return "Hello from main"

def other(func):
    print(helloThere())

other(hello)

# Decorators

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF DECORATOR")

# Its the same thing as 
# func_needs_decorator = new_decorator(func_needs_decorator

func_needs_decorator()