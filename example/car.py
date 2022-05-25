class Car(object):
    def __init__(self,name,color,speed,value):
        self.name=name
        self.color=color
        self.speed=speed
        self.value=int(value)
        
    def Sel(self):
        return "{0}의 속도는 {2}km,".format(self.name,self.color,self.speed,self.value)
    
    def SpeedUp(self):
        if self.value > 0:
            print("{1}{0}의 속도가 {3}km 올라갔습니다.".format(self.name,self.color,self.speed,self.value))
    def SpeedDown(self):
        if self.value <=0:
            print("{1}{0}의 속도가 {3}km 올라갔습니다.".format(self.name,self.color,self.speed,self.value))
            
class Sedan(Car):
    def __init__(self,name,color,speed,value,seats):
        Car.__init__(self,name,color,speed,value)
        self.seats=seats
    
    def __str__(self):
        
        return Car.Sel(self) + "좌석 수는 {}개 입니다.".format(self.seats)

class Truck(Car):
    def __init__(self,name,color,speed,value,carrying):
        Car.__init__(self,name,color,speed,value)
        self.carrying=carrying
    
    def __str__(self):
        
        return Car.Sel(self) + "총 중량은 {}톤 입니다.".format(self.carrying)

car1=Sedan("Grandeur","검정","100",-30,"4")
car2=Truck("Dump","노랑","60",-30,"50")

print(car1)
print(car2)