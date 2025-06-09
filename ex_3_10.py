class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if value <= 100:
            self.__speed = value
        else:
            print("ความเร็วห้ามเกิน 100")
            
    def drive(self):
        print(f"รถวิ่งด้วยความเร็ว {self.__speed} km/h")
        
c = Car("Toyota", 150)
c.speed = 200
c.speed = 170
c.drive()