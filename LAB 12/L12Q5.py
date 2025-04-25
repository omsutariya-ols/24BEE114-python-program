print("OM SUTARIYA")
print("24BEE114")
from datetime import datetime, timedelta

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.time = timedelta(hours=hour, minutes=minute, seconds=second)

    def __str__(self):
        total_seconds = int(self.time.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def add(self, hours=0, minutes=0, seconds=0):
        self.time += timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def subtract(self, hours=0, minutes=0, seconds=0):
        self.time -= timedelta(hours=hours, minutes=minutes, seconds=seconds)

    def difference(self, other):
        return abs(self.time - other.time)

    def is_equal(self, other):
        return self.time == other.time

    def is_greater_than(self, other):
        return self.time > other.time

    def is_less_than(self, other):
        return self.time < other.time

time1 = Time(5, 30, 15)
time2 = Time(3, 45, 30)
time3 = Time(5, 30, 15)

print("Time 1:", time1)
print("Time 2:", time2)
print("Time 3:", time3)

time1.add(1, 15, 30)
print("Time 1 after addition:", time1)

time2.subtract(0, 30, 15)
print("Time 2 after subtraction:", time2)

print("Difference between Time 1 and Time 2:", time1.difference(time2))
print("Time 1 and Time 3 are equal:", time1.is_equal(time3))
print("Time 1 is greater than Time 2:", time1.is_greater_than(time2))
print("Time 1 is less than Time 2:", time1.is_less_than(time2))
