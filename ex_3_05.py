class Animal:
    def __init__(self, sound):
        self.__sound = sound
        
    def set_sound(self, new_sound):
        if new_sound:
            self.__sound = new_sound
        else:
            print("ไม่สามารถตั้งเสียงว่างได้")
            
    def get_sound(self):
        return self.__sound
    
animal = Animal("ร้อง")
animal.set_sound("")
animal.set_sound("เห่า")
print(animal.get_sound())