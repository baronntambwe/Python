import name_and_main

print("Top level name_and_main.1.py")

name_and_main.func()

if __name__ == "__main__":
        print("name_and_main.1.py is being run directly")
else:
        print("name_and_main.1.py is being imported")