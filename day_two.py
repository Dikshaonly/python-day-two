# OOP Concept class and object
# class Robot: 
#     new_var =  "this is token"

# robot  = Robot()
# print(robot.new_var) 

# constructor
# class  Fruit:
#     def __init__(self, name:str, price: int):
#         self.name = name
#         self.price  = price

#     def __str__(self) -> str:
#         return f"this fruit is {self.name} and price is {self.price}"
    
#     def getFruitValue(self):
#         return "this is fruit value funtion"
        
# fruit = Fruit("apple",255)
# fruit1 = Fruit("orange",205)
# print(fruit.getFruitValue())
# print(fruit1)

# inheritance
# class Music:
#     def playMusic(self):
#         return "Music has been started"
    
# class Guitar(Music):
#     def guitarMusic(self):
#         return "Jhing jhing"

# guitar = Guitar() 
# print(guitar.guitarMusic())
# print(guitar.playMusic())

# static method
# class StaticExample():
#     # @staticmethod this is called annotations
#     @staticmethod
#     def guitarMusic():
#         return "Jhing jhing"

# print(StaticExample.guitarMusic())

# encapulation
class EncapsluatedClass:
    def __init__(self,name,age):
        self.name = name
        self._age = age  #protected attribute

    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if age>0:
            self._age = age

my_entry = EncapsluatedClass('Hari',23)
print(f"Name: {my_entry.name}")
print(f"age: {my_entry.age}") #invalid
print(f"age: {my_entry.get_age()}")


