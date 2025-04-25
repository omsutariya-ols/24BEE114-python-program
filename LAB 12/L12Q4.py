print("OM SUTARIYA")
print("24BEE114")
import math

class RegularShape:
    def __init__(self, shape_type, *dimensions):
        
        self.shape_type = shape_type.lower()
        self.dimensions = dimensions

    def perimeter(self):
        
        if self.shape_type == 'square':
            side = self.dimensions[0]
            return 4 * side
        elif self.shape_type == 'circle':
            radius = self.dimensions[0]
            return 2 * math.pi * radius
        elif self.shape_type == 'regular_polygon':
            side_length, num_sides = self.dimensions
            return side_length * num_sides
        else:
            raise ValueError("Unsupported shape type")

    def area(self):
        
        if self.shape_type == 'square':
            side = self.dimensions[0]
            return side ** 2
        elif self.shape_type == 'circle':
            radius = self.dimensions[0]
            return math.pi * (radius ** 2)
        elif self.shape_type == 'regular_polygon':
            side_length, num_sides = self.dimensions
            apothem = side_length / (2 * math.tan(math.pi / num_sides))
            return (num_sides * side_length * apothem) / 2
        else:
            raise ValueError("Unsupported shape type")

# Example usage
if __name__ == "__main__":
    try:
        # Square with side length 5
        square = RegularShape('square', 5)
        print(f"Square Perimeter: {square.perimeter()} units")
        print(f"Square Area: {square.area()} square units")

        # Circle with radius 7
        circle = RegularShape('circle', 7)
        print(f"\nCircle Perimeter: {circle.perimeter()} units")
        print(f"Circle Area: {circle.area()} square units")

        # Regular Hexagon with side length 6
        hexagon = RegularShape('regular_polygon', 6, 6)
        print(f"\nRegular Hexagon Perimeter: {hexagon.perimeter()} units")
        print(f"Regular Hexagon Area: {hexagon.area()} square units")

    except ValueError as e:
        print(e)
