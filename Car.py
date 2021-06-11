class Car:
    def __init__(self, model,color,company,speedLimit):
        self.color = color
        self.company = company
        self.model = model
        self.speedLimit = speedLimit

    def start(self):
       return("start")

    def stop(self):
        print("stop")

    def accelerate(self):
        print("accelerate")

    def change_gear(self, gear_type):
        print("change_gear")


audi = Car('xyz','black','abc',500)

ciaz = Car('xyz','black','abc',500)
