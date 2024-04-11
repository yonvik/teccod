class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def distance_to(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5

point1 = Point(1, 2)
point2 = Point(4, 6)

print("Координаты точки 1:", point1.get_coordinates())
print("Координаты точки 2:", point2.get_coordinates())

distance = point1.distance_to(point2)
print(f"Расстояние между точками 1 и 2: {distance}")
