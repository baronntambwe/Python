
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
print(x())

# Function as argument

def helloThere():
    return "Hello from main"

def other(func):
    print(helloThere())

other(hello)