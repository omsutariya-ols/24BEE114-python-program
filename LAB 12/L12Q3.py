print("OM SUTARIYA")
print("24BEE114")
import math

class Solid:
    def __init__(self, solid_type, *dimensions):
        
        self.solid_type = solid_type.lower()
        self.dimensions = dimensions

    def volume(self):
        
        if self.solid_type == 'cube':
            side = self.dimensions[0]
            return side ** 3
        elif self.solid_type == 'sphere':
            radius = self.dimensions[0]
            return (4/3) * math.pi * (radius ** 3)
        elif self.solid_type == 'cylinder':
            radius, height = self.dimensions
            return math.pi * (radius ** 2) * height
        else:
            raise ValueError("Unsupported solid type")

    def surface_area(self):
        
        if self.solid_type == 'cube':
            side = self.dimensions[0]
            return 6 * (side ** 2)
        elif self.solid_type == 'sphere':
            radius = self.dimensions[0]
            return 4 * math.pi * (radius ** 2)
        elif self.solid_type == 'cylinder':
            radius, height = self.dimensions
            return 2 * math.pi * radius * (radius + height)
        else:
            raise ValueError("Unsupported solid type")

if __name__ == "__main__":
    try:
        # Cube with side length 3
        cube = Solid('cube', 3)
        print(f"Cube Volume: {cube.volume()} units³")
        print(f"Cube Surface Area: {cube.surface_area()} units²")

        # Sphere with radius 5
        sphere = Solid('sphere', 5)
        print(f"\nSphere Volume: {sphere.volume()} units³")
        print(f"Sphere Surface Area: {sphere.surface_area()} units²")

        # Cylinder with radius 3 and height 7
        cylinder = Solid('cylinder', 3, 7)
        print(f"\nCylinder Volume: {cylinder.volume()} units³")
        print(f"Cylinder Surface Area: {cylinder.surface_area()} units²")

    except ValueError as e:
        print(e)
