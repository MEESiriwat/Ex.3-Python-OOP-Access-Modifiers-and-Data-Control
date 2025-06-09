class Animal:
    def __init__(self, sound):
        self.__sound = sound
        
    def sound(self):
        return self.__sound
    
animal = Animal("จิ๊บ")
print(animal.sound())