# manipulating numbers

mystring = "I'am here to do things"

#print(mystring[5])
#print(mystring[-1]) #Returns last index

# sliciing

#print(mystring[2:]) 
#print(mystring[:5]) 
#print(mystring[::2])
# strings are imutable: mystring[5] = 'x'

# methods

s = mystring.upper()

# format

s = "I wanna format this string with: {x} and an {y}".format(x = "a method", y = "argument")
s = "I wanna format this string with: {} and an {}".format("a method", "argument")
print(s)

