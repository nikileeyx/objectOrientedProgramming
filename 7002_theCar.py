class Car:
  def __init__(self, brand, colour, speed):
    self.brand = brand
    self.colour = colour
    self.speed = speed
    
  def whoAmI(self):
    print("Hi I am a " + self.colour + " car")
    
  def upgrade(self, speed):
    speed += 10
    print("Your speed has increased by " + str(self.speed))
    return speed
    


'''
Pass in to Python Shell these commands

car = Car("hello", "yellow", "10")
car.whoAmI()

'''
