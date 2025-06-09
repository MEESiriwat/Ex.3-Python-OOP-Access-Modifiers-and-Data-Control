class Animal:
    def __init__(self, name, species):
        self.name = name
        self._species = species
        
animal = Animal("แมว", "สัตว์เลี้ยงลูกด้วยนม")
print(animal._species)  