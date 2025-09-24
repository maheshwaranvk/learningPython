#https://www.geeksforgeeks.org/problems/rank-scores/1
import pandas as pd
scores = [
    [1, 9.50],
    [2, 8.75],
    [3, 9.25],
    [4, 7.85],
    [5, 8.75],
    [6, 9.00]
]

scoresDF = pd.DataFrame(scores, columns=['id','score'])
print(scoresDF)

sortedScore=scoresDF.sort_values(by='score')
print(sortedScore[::-1])
rankedScore = {
    'Score' : sortedScore[::-1]['score'],
    'Rank'  : [1,2,3,4,5,6]
}
print(pd.DataFrame(rankedScore))