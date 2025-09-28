import matplotlib.pyplot as plt


testCaseStatus = ['Passed','Failed','Skipped']
testCaseCount = [45,10,5]


plt.bar(testCaseStatus, testCaseCount, width=0.25)


plt.title('Test Execution Results')
plt.xlabel('Test Status')
plt.ylabel('Number of Test Cases')
plt.grid(True)
plt.legend()
plt.show()