class Student:
    def __init__(self, score):
        self.__score = score
        
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            print("คะแนนต้องอยู่ระหว่าง 0 ถึง 100")
            
s = Student(85)
s.score = 110
s.score = 95
print(s.score)