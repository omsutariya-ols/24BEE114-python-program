print("name: om sutariya")
print("roll no.: 24bee114")
x_c = float(input("enter the x-coordinate of the center: "))
y_c = float(input("enter the y-coordinate of the center: "))
r = float(input("enter the radius of the circle: "))
x_p = float(input("enter the x-coordinate of the point: "))
y_p = float(input("enter the y-coordinate of the point: "))
distance_squared = (x_p - x_c) ** 2 + (y_p - y_c) ** 2
radius_squared = r ** 2
if distance_squared < radius_squared:
    print("the point is inside the circle.")
elif distance_squared == radius_squared:
    print("the point is on the circle.")
else:
    print("the point is outside the circle.")
