print("OM SUTARIYA")
print("24BEE114")
class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)

if __name__ == "__main__":
    c1 = ComplexNumber(3, 2)
    c2 = ComplexNumber(1, 7)

    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f"Addition: {c1 + c2}")
    print(f"Subtraction: {c1 - c2}")
    print(f"Multiplication: {c1 * c2}")
    print(f"Division: {c1 / c2}")
