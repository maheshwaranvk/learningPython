class Employee:
    def __init__(self, name):
        self.name = name

class AutomationSkills:
    def writeScript(self):
        print("Writing Selenium Scripts")

class AutomationTester(Employee, AutomationSkills):
    def __init__(self, name):
        super().__init__(name)
    def executeTests(self):
        print("Executing the tests")

p1 = AutomationTester("Mahesh")
p1.writeScript()
p1.executeTests()