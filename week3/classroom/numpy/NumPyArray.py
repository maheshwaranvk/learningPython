import numpy as np

exectuionTimes = np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("First Element : ", exectuionTimes[0])
print("Last Element : ", exectuionTimes[-1])
print("Third Element : ", exectuionTimes[2])
print("Shape of the array : ", exectuionTimes.shape)

for (index,seconds) in enumerate(exectuionTimes,start=1):
    print(f"Test {index} execution time: {seconds} seconds")

print(exectuionTimes.reshape(2,4))

exectuionTimes2 = np.array([50,55,60,65])
AllexecutionTime = np.concatenate([exectuionTimes, exectuionTimes2])

print(np.split(AllexecutionTime,3))