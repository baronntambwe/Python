class Dog():

    # CLASS OBJECT ATTRIBUTE

    spicies = "Carnivore"


    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
    
    def say(self):
        phrase = self.name + " is a " + Dog.spicies
        return phrase


dog = Dog("Domestique", "Imbwa")
print(dog.breed)
print(dog.say())