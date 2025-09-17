#https://drive.google.com/open?id=1_NYQQ0btSf8NMQ92Eoa5eUwUcc_3CM8P&usp=drive_fs

import numpy as np
class ManualTester:
    def analyze(self, data):
        print("First Five execution times : ", data[:5])
    
class AutomationTester():
    def analyze(self, data):
        print("Fastest Execution : ", data.min())

class PerformanceTester():
    def analyze(self, data):
        print("95th percentile execution time : ", np.percentile(data, 95))

def show_analysis(tester, data):
    tester.analyze(data)

data = np.array([10,20,43,45,21,65,24,46,23,34,26,56])
p1 = ManualTester()
show_analysis(p1, data)
show_analysis(AutomationTester(), data)
show_analysis(PerformanceTester(), data)