class car:
    def __init__(self,manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color
    def accelerate(self):
        print(self.manufacturer,self.model,"is moving")
    
    def stop(self):
        print(self.manufacturer,self.model,"has stopped")


Car1 = car("Hyundai","Venue","2024","Manual","Titan Grey")
Car2 = car("Tata","Verna","2025","Manual","Black")
Car3 = car("Maruti", "800", "2013", "Manual", "Red")

Car1.accelerate()
Car2.stop()