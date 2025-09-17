#https://drive.google.com/open?id=1roraXdOgNDahbJOpUkMlk0w9Ba8lels3&usp=drive_fs

import numpy as np
class TestReport:
   # executionTimes=np.array([13,14,52,23,45])
    def __init__(self, executionTimes):
        self.data = np.array(executionTimes)

    def averageTime(self):
        return np.mean(self.data)
    
    def maxTime(self):
        return np.max(self.data)

class RegressionReport(TestReport):
    def __init__(self, executionTimes):
        super().__init__(executionTimes)
    
    def slowTests(self, threshold):
        return self.data[self.data<threshold]
    
obj = RegressionReport([13,14,52,23,45])
print("Average Run Time : ", obj.averageTime())
print("Maximum Execution Time : ", obj.maxTime())
print("slow tests : ", obj.slowTests(30))