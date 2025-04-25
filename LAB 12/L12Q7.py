print("OM SUTARIYA")
print("24BEE114")
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters


