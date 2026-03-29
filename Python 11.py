# Question no 1

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(self.name, "-", self.author + ",", self.pages, "pages")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(self.name, "- Chief editor:", self.chief_editor)


# main program
donald = Magazine("Donald Duck", "Aki Hyyppä")
compartment = Book("Compartment No. 6", "Rosa Liksom", 192)

donald.print_information()
compartment.print_information()

# QUESTION NO 2

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.speed = 0
        self.km = 0

    def drive(self, hours):
        self.km += self.speed * hours


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume


# main program
e_car = ElectricCar("ABC-15", 180, 52.5)
g_car = GasolineCar("ACD-123", 165, 32.3)

e_car.speed = 120
g_car.speed = 100

e_car.drive(3)
g_car.drive(3)

print("Electric car km:", e_car.km)
print("Gasoline car km:", g_car.km)
