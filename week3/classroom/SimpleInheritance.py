class Employee:
    def __init__(self, name, employeeId):
        self.name=name
        self.employeeId=employeeId
    
class Tester(Employee):
    def _init__(self, name, employeeId):
        super().__init__(name, employeeId)
    
    def runTests(self):
        print(f"{self.name}/{self.employeeId} is running automation tests")

p1 = Tester("Mahesh", "E1")
p1.runTests()