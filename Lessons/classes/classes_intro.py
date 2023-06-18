# class Dog:
    
#     # Class specific attribute which is not object specific
#     animal_kind = "canine"
    
#     # Class method with "name" as a parameter
#     def bark(self, name):
#         return "woof " + name

# # Instantiation of an object 
# laika = Dog()



# class Dog_evolved:
        
#     def __init__(self, name, colour) -> None:
#         self.name = name
#         self.colour = colour
#         self.animal_kind = "canine"
#         print(self.bark())  # Will run the method when object initialised
        
#     def bark(self):
#         return "woof " + self.name
    
# laika = Dog_evolved("Laika", "gold")


class Animal:
    
    def __init__(self) -> None:
        self.alive = True
        self.eyes = True
        
    def breathe(self):
        print("one breath in, one out")
        

class Dog(Animal):
    
    def __init__(self) -> None:
        super().__init__()
        self._eyes = 2
        
    def bark():
        print("woof")
    
    # Encapsulation to limit access to class attributes
    def get_eyes(self):
        return self._eyes

    # Encapsulation to limit access to class attributes   
    def set_eyes(self, number):
        self._eyes = number
        
laika = Dog()
