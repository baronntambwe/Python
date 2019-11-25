

def my_func(param="default"):
    return "hellow"

response = my_func()
print(response)

# Lambda

my_list = [1,2,3,4,5,6,7,8,9]

events = filter(lambda num: num%2 == 0, my_list)
print(list(events))