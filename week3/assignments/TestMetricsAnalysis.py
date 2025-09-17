#https://drive.google.com/open?id=17_lBEaINiFiJVjv72DEs0hipiOKwE_90&usp=drive_fs

import numpy as np
data = np.random.randint(5,50,size=(5,5))
print (data)

def statisticalAnalysis():
    for i in range(0,data.shape[0]-1):
        averageExecutionTime = np.mean(data[i][:])
        print(f"{i+1} Cycle Average Execution Time", int(averageExecutionTime))
        print(f"Standard Deviation of {i+1} Cycle", np.std(data[i][:]))
    print("TestCase with maximum execution time",data.max())

def slicingOperations():
    print("First 10 test execution times from Cycle 1", (data[0][:])[:10])
    print("First 5 test execution times from Cycle 5", (data[4][:])[:5])
    print("Alternate test from Cycle 3", (data[2][:]))
    print("Alternate test from Cycle 3", (data[2][:])[::2])

def arithmeticOperations():
    print ("Addition of Cycle 1 and Cycle 2", data[0][:] + data[1][:])
    print ("Subraction of Cycle 1 and Cycle 2", data[0][:] - data[1][:])
    print ("Multiplication of Cycle 4 and Cycle 5", data[3][:] * data[4][:])
    print ("Division of Cycle 4 and Cycle 5", data[3][:] / data[4][:])

def powerOperations():
    print ("Square of each element", np.power(data,2))
    print ("Cube of each element", np.power(data,3))
    print ("Cube of each element", np.sqrt(data))
    print ("log of each element", np.log(data))

def copyOperations():
    shallowCopy=data.view()
    deepCopy=data.copy()
    data[0][1]=14
    print(shallowCopy)
    print(deepCopy)

def filteringConditions():
    higherThan30Sec = data[1][:]>30
    print("in Cycle 2 > 30 seconds", data[1][:][higherThan30Sec])
    higherThan25Sec = data>25
    print("in every cycle greate than 25 seconds", data[higherThan25Sec])
    print ("replacing all execution times less than 10 to threashold value 10")
    data[data<10]=10
    print ("updated execution times", data)

if __name__ =="__main__":
    statisticalAnalysis()
    slicingOperations()
    arithmeticOperations()
    powerOperations()
    copyOperations()
    filteringConditions()