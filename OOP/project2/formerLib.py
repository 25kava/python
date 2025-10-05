import math

class customException(Exception):
    pass

class rektangel:
    def __init__(self, height: float, base: float, unit: str):
        self.base = base
        self.height = height
        self.unit = unit

    def calcArea(self):
        Area = self.base * self.height
        print(f"Area = {Area:.2f} {self.unit}²")

    def calcOmkrets(self):
        Omkrets = 2*(self.base) + 2*(self.height)
        print(f"Omkrets = {Omkrets:.2f} {self.unit}")

class triangel(rektangel):
    def calcArea(self):
        Area = (self.base * self.height) / 2
        print(f"Area = {Area:.2f} {self.unit}²")

    def calcOmkrets(self):
        Omkrets = self.base + self.height + (math.sqrt(self.base**2 + self.height**2))
        print(f"Omkrets = {Omkrets:.2f} {self.unit}")

class cirkel:
    def __init__(self, radius, unit):
        self.radius = radius
        self.unit = unit

    def calcArea(self):
        Area = (self.radius**2)*(math.pi)
        print(f"Area = {Area:.2f} {self.unit}²")

    def calcOmkrets(self):
        Omkrets = 2*(self.radius)*(math.pi)
        print(f"Omkrets = {Omkrets:.2f} {self.unit}")