import matplotlib.pyplot as plt

executionTimes = [12, 15, 20, 18, 22, 30, 25, 16, 19, 28, 24, 14]
plt.hist(executionTimes, bins=5)

plt.xlabel("Duration (seconds)")
plt.ylabel("Number of Test Cases")
plt.show()