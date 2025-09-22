import pandas as pd
import numpy as np

#1
panSeries = pd.Series([12,15,20,18,25,30,22])
print(panSeries)

#2
middleIndex = int(len(panSeries)/2)
startingIndex = int((3-1)/2)
endingIndex = middleIndex + int((3-1)/2)

print(panSeries[startingIndex:endingIndex])
print(panSeries.iloc[startingIndex:endingIndex])

numpyArray = np.array([20,30,40])
panSeries1 = pd.Series(numpyArray)
print(panSeries1)

#3
engineers = {
    'Alex':500,
    'Steve':200,
    'Bob':300
}

dictionarySeries = pd.Series(engineers)
print(dictionarySeries)