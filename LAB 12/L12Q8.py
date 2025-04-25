print("OM SUTARIYA")
print("24BEE114")
class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def display(self):
        print(self.value)
