import math

class ShapeCalculator:
    def __init__(self):
        pass

    def circle_area(self, radius):
        return math.pi * radius**2

    def triangle_area(self, side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    def is_right_angle_triangle(self, side1, side2, side3):
        sides = [side1, side2, side3]
        max_side = max(sides)
        sides.remove(max_side)
        if max_side**2 == sides[0]**2 + sides[1]**2:
            return True
        else:
            return False

if __name__ == "__main__":
    calculator = ShapeCalculator()
    print("Circle area:", calculator.circle_area(5))
    print("Triangle area:", calculator.triangle_area(3, 4, 5))
    print("Is right angle triangle:", calculator.is_right_angle_triangle(3, 4, 5))
