import matplotlib.pyplot as plt


weeks = [1, 2, 3, 4, 5, 6]
defects = [5, 8, 6, 10, 7, 4]


plt.plot(weeks, defects, marker='D', linestyle='dashed', color='r')


plt.title('Defect Trend Over Time')
plt.xlabel('Week Number')
plt.ylabel('Number of Defects')


plt.grid(True)


plt.show()