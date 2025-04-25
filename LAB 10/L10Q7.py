print("OM SUTARIYA")
print("24BEE114")
import pickle


class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, DOJ: {self.doj}, Salary: {self.salary}"


def serialize_employee(employee, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)
    print(f"Employee object serialized and saved to '{filename}'.")


def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        employee = pickle.load(file)
    print("Employee object deserialized successfully.")
    return employee


emp = Employee(101, "John Doe", "2020-05-15", 50000)
serialize_employee(emp, "employee_data.pkl")


deserialized_emp = deserialize_employee("employee_data.pkl")
print(deserialized_emp)

