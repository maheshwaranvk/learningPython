import csv
class testcase:
    def __init__(self, testId, testName, module, status="Not Executed"):
        self.testId = testId
        self.testName = testName
        self.module = module
        self.status = status

    def executeTest(self, result):
        self.status = result

    def displayTestCase(self):
        print ("Test ID : ", self.testId)
        print ("Test Name : ", self.testName)
        print ("module : ", self.module)
        print ("status : ", self.status)

    def toCSVRow(self):
        print("Write to CSV")

class automatedTestCase(testcase):
    def __init__(self, testId, testName, module, automationTool, status="Not Executed"):
        super().__init__(testId, testName, module, status)
        self.automationTool = automationTool
    
    def displayTestCase(self):
        super().displayTestCase()
        print ("Automation Tool : ", self.automationTool)

    def toCSVRow(self):
        print("Write to CSV")

class testSuite:
    def __init__(self, suiteName):
        self.suiteName = suiteName
    suiteTestCases = []

    def addTest(self, testCase):
        self.suiteTestCases.append(testCase)

    def runAllTests(self):
        for i in self.suiteTestCases:
            result = input(f"Enter the test result of '{i.testName}': ")
            i.executeTest(result)
    
    def saveResultsToCSV(self):
        with open('testresults.csv','w',newline='') as file :
            fieldNames = ['Test ID', 'Test Name', 'Module', 'Status', 'Automation Tool']
            writer = csv.DictWriter(file, fieldnames=fieldNames)
            writer.writeheader()
            for tc in self.suiteTestCases:
                writer.writerow({
                    'Test ID': tc.testId,
                    'Test Name': tc.testName,
                    'Module' : tc.module,
                    'Status' : tc.status,
                    'Automation Tool': getattr(tc, 'automationTool', 'NA')
                })

    def summaryReport(self):
        print("Total number of testcases : ",len(self.suiteTestCases))
        passedTests = []
        failedTests = []
        notExecutedTests = []
        for testcase in self.suiteTestCases:
            if (testcase.status == 'Pass'):
                passedTests.append(testcase)
            elif (testcase.status == 'Fail'):
                failedTests.append(testcase)
            else:
                notExecutedTests.append(testcase)
        print("*****************************************")
        if (len(passedTests)==0):
            print("No Passed Testcases")
        else:
            print("Passed TestCases")
            for tc in passedTests:
                tc.displayTestCase()

        print("*****************************************")
        if (len(failedTests)==0):
            print("No Failed Testcases")
        else:
            print("Failed TestCases")
            for tc in failedTests:
                tc.displayTestCase()

        print("*****************************************")
        if (len(notExecutedTests)==0):
            print("All tests were executed")
        else:
            print("Non Executed TestCases")
            for tc in notExecutedTests:
                tc.displayTestCase()


if __name__=="__main__":
    m1 = testcase(1, "Manual_Login", "iOS")
    m2 = testcase(2, "Manual_Employee", "iOS")

    a1 = automatedTestCase(3, "Automated_Login", "iOS", "Selenium")
    a2 = automatedTestCase(4, "Automated_Employee", "iOS", "Playwright")

    ts1 = testSuite("Smoke Test")
    ts1.addTest(m1)
    ts1.addTest(m2)
    ts1.addTest(a1)
    ts1.addTest(a2)
    ts1.runAllTests()
    ts1.summaryReport()
    ts1.saveResultsToCSV()