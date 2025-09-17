#https://drive.google.com/open?id=1lDoPZEIExgsbLLX2ukeXi6ubG6EMjvUb&usp=drive_fs

class Employee:
    def __init__(self, name, empId, department):
        self.name=name
        self.empId=empId
        self.department=department

    def displayInfo(self):
        print("Employee name : ", self.name)
        print("Employee ID : ", self.empId)
        print("Employee department : ", self.department)
    
class Manager(Employee):
    def __init__(self, name, empId, department,teamSize):
        super().__init__(name, empId, department)
        self.teamSize=teamSize
    
    def displayInfo(self):
        super().displayInfo()
        print("Team Size : ", self.teamSize)
    
class Developer(Employee):
    def __init__(self, name, empId, department, programmingLanguage):
        super().__init__(name, empId, department)
        self.programmingLanguage=programmingLanguage
    
    def displayInfo(self):
        super().displayInfo()
        print("Programming Language : ", self.programmingLanguage)

if __name__=="__main__":
    obj1=Manager("Mahesh","45","Testing","6")
    obj1.displayInfo()

    obj2=Developer("Thiru","23","Developer","C#")
    obj2.displayInfo()