class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color=color
        self.company=company
        self.model=model
        self.speedLimit=speedLimit
    def start(self):
        print("started")
    def stop(self):
        print("stop")    
    def accelerate(self):
        print("accelerating")
    def changeGear(self,gearType):
        print("gearChanged")
audi=Car("a6","red","audi",80)
print(audi.stop())
