class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employeeId):
        super().__init__(name)
        self.employeeId = employeeId

class Manager(Employee):
    def __init__(self, name, employeeId, teamSize):
        super().__init__(name, employeeId)
        self.teamSize=teamSize
    
    def showDetails(self):
        print("Employee Name : ", self.name)
        print("Employee ID : ", self.employeeId)
        print("Team Size : ", self.teamSize)

p1 = Manager("Mahesh", "E1", 6)
p1.showDetails()