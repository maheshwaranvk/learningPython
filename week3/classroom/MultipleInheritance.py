class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employeeId):
        self.employeeId = employeeId

class Manager(Person, Employee):
    def __init__(self, name, employeeId, teamSize):
        Person.__init__(self, name)
        Employee.__init__(self, employeeId)
        self.teamSize=teamSize
    
    def showDetails(self):
        print("Employee Name : ", self.name)
        print("Employee ID : ", self.employeeId)
        print("Team Size : ", self.teamSize)

p1 = Manager("Mahesh", "E1", 6)
p1.showDetails()