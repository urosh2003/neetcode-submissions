class Car:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append(Car(position[i],speed[i]))

        cars.sort(key=lambda i: i.position)

        stack = []
        fleets = len(cars)
        lastTime = -1

        for i in range(len(cars)-1,-1,-1):
            time = (target-cars[i].position) / cars[i].speed
            if time <= lastTime:
                fleets -= 1
            else:
                lastTime = time

        return fleets

