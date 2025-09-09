class primeNum:
    printNumbers = [2, 5, 3, 11, 7, 13, 17, 19, 23, 29]
    
    def reverseOrder(self):
        primeNumReverse = self.printNumbers[::-1]
        print("Print number reverse")
        print (primeNumReverse)
    
    def descendingOrder(self):
        sortedPrime = sorted(self.printNumbers)
        descendingOrderPrime = sortedPrime[::-1]
        print("Print descending")
        print (descendingOrderPrime)
    
    def lastThreePrimeNumbers(self):
        lastThreePrime=[]
        count=1
        index=-1
        while (count<=3):
            lastThreePrime.append(self.printNumbers[index])
            count=count+1
            index=index-1
        print("Print last three prime numbers")
        print(lastThreePrime)
    
    def getEverySecondPrime(self):
        secondPrimeNumber=[]
        for index, value in enumerate(self.printNumbers):
            if(index%2==0):
                secondPrimeNumber.append(value)
        print("Print every second prime numbers")
        print(secondPrimeNumber)

    def middlePrimes(self, count):
        middleFivePrimes=[]
        middleIndex = len(self.printNumbers)//2
        startingIndex = (count-1)//2
        endingIndex = middleIndex + (count-1)//2
        #for index, value in enumerate(self.printNumbers):
            #if (index >= startingIndex and index <=endingIndex):
             #   middleFivePrimes.append(value)
        print("Print middle five prime numbers", self.printNumbers[startingIndex:endingIndex] )
        #print(middleFivePrimes)

obj = primeNum()
obj.reverseOrder()
obj.descendingOrder()
obj.lastThreePrimeNumbers()
obj.getEverySecondPrime()
obj.middlePrimes(5)