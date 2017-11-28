class Car(object):
    def  __init__(self, price, speed, fuel,mileage):
        self.price = price
        if price < 10000:
           self.tax = .12           
        else:
           self.tax =.15
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()   

    def display_all(self):
        print 'Price: $' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + str(self.fuel) 
        print 'Mileage: ' + str(self.mileage) + ' mpg'
        print 'Tax ' + str(self.tax)




#Run Methods
car1 = Car(1000, 5, 'Full', 20)
car2 = Car(2000, 10, 'Not Full', 30)
car3 = Car(3000, 15, 'Not Full', 40)
car4 = Car(4000, 20, 'Full', 50)
car5 = Car(5000, 25, 'Not Full', 60)
car6 = Car(20000000, 30, 'Full', 70)