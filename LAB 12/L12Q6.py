print("OM SUTARIYA")
print("24BEE114")
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]
    def __eq__(self, other):
        return self.date == other.date
