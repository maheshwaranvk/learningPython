class Student:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    #to print all the information
    def printStudentInfo(self):
        print("Student name : ",self.name)
        print("Student grade : ",self.grade)
        print("Student department : ",self.department)
    
    #update the grade
    def updateStudentGrade(self, newGrade):
        self.grade = newGrade
    
if __name__ == "__main__":
    s1 = Student("Mahesh", "D", "CSE")
    s2 = Student("Siva", "S", "CSE")
    s3 = Student("Aruvi", "S+", "IT")

    s1.printStudentInfo()
    s2.printStudentInfo()
    s3.printStudentInfo()

    s2.updateStudentGrade("S++")
    print("new s2 record : ")
    s2.printStudentInfo()