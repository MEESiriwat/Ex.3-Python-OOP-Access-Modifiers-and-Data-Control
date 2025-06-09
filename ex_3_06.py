class Animal:
    def __init__(self, sound):
        self.__sound = sound
        
    @property
    def sound(self):
        return self.__sound
    
    
    @sound.setter
    def sound(self, value):
        if value != "":
            self.__sound = value
        else:
            print("ไม่สามารถตั้งเสียงว่างได้")
            
animal = Animal("ร้อง")
print(animal.sound)
animal.sound = "เห่า"
print(animal.sound)