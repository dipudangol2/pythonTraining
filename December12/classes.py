class Vehicle:
    def __init__(self,seats,mileage,top_speed):
        self.seats = seats
        self.mileage = mileage
        self.top_speed = top_speed
        self.covered_length = 0
    
    
    def give_seats(self):
        print(f"There are {self.seats} seats in the car.")
        
        
    def give_mileage(self):
        print(f"The car covers {self.mileage}km on one litre of fuel.")
        
        
    def give_top_speed(self):
        print(f"The car has maximum speed of  {self.top_speed}kmph.")
        
        
    def drive(self):
        self.covered_length += 1
        # print(f'{self.covered_length} km run.')
    
    
    def driven_distance(self):
        print(f'The car has driven {self.covered_length} km.')
        
        
        
class Electic_Car(Vehicle):
    def __init__(self,seats,mileage,top_speed,model,b_cap):
        super().__init__(seats,mileage,top_speed)
        self.b_cap = b_cap
        self.model = model
    
    
    def charge(self,hours):
        self.b_cap += hours*10 


car1 = Vehicle(4,30,145)
car2 = Vehicle(2,20,200)
car3= Electic_Car(4,30,140,'Tesla',20)
driving_distance = 50

car3.give_seats()
car3.give_top_speed()
car3.give_mileage()
print(car3.model)
print(car3.b_cap)

car3.charge(4)

print(car3.b_cap)

car1.give_seats()
car2.give_seats()
while True:
    car1.drive()
    driving_distance -= 1
    if driving_distance <= 0:
        break
    
car1.driven_distance()