#https://www.geeksforgeeks.org/problems/second-highest-salary/1

import pandas as pd

data = [
    [1, 1200],
    [2, 3500],
    [3, 4800],
    [4, 2900],
    [5, 5000],
    [6, 4300]
]

dataDf = pd.DataFrame(data, columns=['id','salary'])
secondHighestSalary = dataDf.sort_values(by="salary").reset_index(drop=True)
print(secondHighestSalary.iloc[1])