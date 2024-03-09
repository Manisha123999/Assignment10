import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance_covered = 0

    def drive(self):
        self.distance_covered += self.speed

    def __str__(self):
        return f"{self.name:<10} {self.speed:>6} km/h {self.distance_covered:>8} km"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-20, 20)
            car.drive()

    def print_status(self):
        print(f"{'Car':<10} {'Speed':>6} {'Distance':>8}")
        print("-" * 30)
        for car in self.cars:
            print(car)
        print()

    def race_finished(self):
        for car in self.cars:
            if car.distance_covered >= self.distance:
                return True
        return False


# Create cars for the race
car_names = ["Car1", "Car2", "Car3", "Car4", "Car5", "Car6", "Car7", "Car8", "Car9", "Car10"]
cars = [Car(name, random.randint(100, 200)) for name in car_names]

# Create the race
race = Race("Grand Demolition Derby", 8000, cars)

# Simulate the race
print("Race Start!")
race.print_status()

hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1
    if hours_passed % 10 == 0:
        race.print_status()

print("Race Finished!")
race.print_status()