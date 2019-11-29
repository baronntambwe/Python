
try:
    fs = open("simple.txt","r")
    fs.write("Hello text")
except IOError:
    print("Could not find the file")
else:
    print("Success!")
    fs.close()