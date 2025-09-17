import numpy as np
threeDime = np.array(
    [
        [[1,2,3],
         [4,5,6]
         ],
     [
         [7,8,9],
         [10,11,12]]
         ])

print(threeDime[0][0][0])
print(threeDime[0][1][1])
print(threeDime[1][1][2])

print(threeDime.ndim)