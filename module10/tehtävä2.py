
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def go_to_floor(self, target):
        while self.floor < target:
            self.floor += 1
            print("Floor:", self.floor)

        while self.floor > target:
            self.floor -= 1
            print("Floor:", self.floor)


class Building:
    def __init__(self, bottom, top, number):
        self.elevators = []

        for i in range(number):
            self.elevators.append(Elevator(bottom, top))

    def use_elevator(self, number, target):
        self.elevators[number - 1].go_to_floor(target)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(1)


building = Building(1, 10, 3)
building.use_elevator(1, 5)
building.use_elevator(2, 8)
