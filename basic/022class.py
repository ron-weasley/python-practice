class Circle:
    m = 2
    n = "lol"

    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

    def print(self):
        return "  ".join(self.n for i in range(self.m))


NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())
print(NewCircle.print())
