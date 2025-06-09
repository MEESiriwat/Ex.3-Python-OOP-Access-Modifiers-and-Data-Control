class Animal:
    def __init__(self, name, sound):
        self.name = name
        self._sound = sound
        
    def make_sound(self):
        print(self._sound)
        
animal = Animal("หมา", "โฮ่ง")
animal.make_sound()