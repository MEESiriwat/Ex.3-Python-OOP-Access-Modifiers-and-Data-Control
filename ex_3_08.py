class Employee:
    def __init__(self, salary):
        self.__salary = salary
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("เงินเดือนไม่ควรติดลบ")
            
    def get_bonus(self):
        return self.__salary * 0.1
    
emp = Employee(30000)
print("โบนัส:", emp.get_bonus())