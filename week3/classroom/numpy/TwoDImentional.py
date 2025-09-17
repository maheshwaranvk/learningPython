import numpy as np

twoDime = np.array([[1,2,3,5],[4,5,6,8]])
print(twoDime[0][1])
print(twoDime[1][1])
print(twoDime[0][2])
sum=0
for value in twoDime:
    for anotherValue in value:
        sum=sum+anotherValue
print(sum)

print(twoDime.ndim)