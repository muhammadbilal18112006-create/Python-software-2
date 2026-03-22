# QUESTION NO 1

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"\nMoving to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Arrived at floor {target_floor}\n")


# Main program
def main():
    h = Elevator(0, 10)
    h.go_to_floor(5)
    h.go_to_floor(0)


main()

#QUESTION NO 2

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"\nMoving to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {target_floor}\n")


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.elevators = []
        for i in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number}...")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)


# Main program
def main():
    house = Building(0, 10, 3)
    house.run_elevator(1, 7)
    house.run_elevator(2, 3)
    house.run_elevator(1, 0)


main()

# QUESTION NO 3

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"\nMoving to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {target_floor}\n")


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.elevators = []
        for _ in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        print(f"\nRunning elevator {elevator_number}...")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\n🚨 FIRE ALARM! All elevators moving to bottom floor...")
        for index, elevator in enumerate(self.elevators, start=1):
            print(f"\nElevator {index}:")
            elevator.go_to_floor(elevator.bottom_floor)
        print("All elevators are now at the bottom floor.\n")


# Main program
def main():
    house = Building(0, 10, 3)
    house.run_elevator(1, 7)
    house.run_elevator(2, 4)
    house.fire_alarm()


main()

# QUESTION NO 4

import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change

        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n=== Race Status: {self.name} ===")
        print(f"{'Reg.Nr':<10} {'Max(km/h)':<12} {'Speed':<10} {'Distance':<12}")
        print("-" * 50)

        for c in self.cars:
            print(f"{c.registration_number:<10} "
                  f"{c.maximum_speed:<12} "
                  f"{c.current_speed:<10} "
                  f"{c.travelled_distance:<12.1f}")

        print("-" * 50)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False


# Main program
def main():
    cars = []
    for i in range(1, 11):
        reg = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(reg, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0

    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        if hours_passed % 10 == 0:
            race.print_status()

    print("\n🏁 THE RACE HAS FINISHED! 🏁")
    race.print_status()


main()

