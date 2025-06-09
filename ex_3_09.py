class Circle:
    def __init__(self, redius):
        self.__redius = redius
        
    @property
    def area(self):
        return 0.5 * self.__redius * self.__redius
    
c = Circle(5)
print("พื้นที่วงกรม", c.area)