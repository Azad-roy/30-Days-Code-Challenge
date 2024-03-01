# 1.Create a class representing a car with attributes like model and color.

class attributes:
    def __init__(self,car,model,color):
        self.car=car
        self.model=model
        self.color=color
        
    def details(self):
        print(f"Name of the car is: {self.car}")
        print(f"Color of the {self.car} is: {self.color}")
        print(f"Model name of the {self.car} is: {self.model}")
        
car,model,color=[str(car) for car in (input("Enter the name of car,model,color in separate: ")).split()]
representing=attributes(car,model,color)
representing.details()