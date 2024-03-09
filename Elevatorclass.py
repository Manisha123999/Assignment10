class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Invalid floor.")
            return

        if floor == self.current_floor:
            print("Already on the requested floor.")
            return

        if floor > self.current_floor:
            self.floor_up(floor)
        else:
            self.floor_down(floor)

    def floor_up(self, floor):
        while self.current_floor < floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}.")

    def floor_down(self, floor):
        while self.current_floor > floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}.")


# Example usage
elevator = Elevator(1, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)