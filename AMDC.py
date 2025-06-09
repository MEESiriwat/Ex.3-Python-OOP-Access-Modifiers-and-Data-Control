class Person:
    def __init__(self):
        self.name = "ศิริวรรษ"
        self._age = 17
        self.__salary = 30000
        
p = Person()
print(p.name)
print(p._age)
print(p._Person__salary) 