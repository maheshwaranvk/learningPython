# Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
# Sample Financial data (fdata.csv):
# Date,Open,High,Low,Close
# 10-03-16,774.25,776.065002,769.5,772.559998
# 10-04-16,776.030029,778.710022,772.890015,776.429993
# 10-05-16,779.309998,782.070007,775.650024,776.469971
# 10-06-16,779,780.47998,775.539978,776.859985
# 10-07-16,779.659973,779.659973,770.75,775.080017 

import matplotlib.pyplot as plt

date = ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16']
open = [774.25, 776.030029, 779.309998, 779, 779.659973]
high = [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
low = [769.5, 772.890015, 775.650024, 775.539978, 770.75]
close = [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]

plt.plot(date,open, linestyle='-', color='b', label = 'open', marker='o', markerfacecolor='r')
plt.plot(date,high, linestyle='-', color='c', label = 'high')
plt.plot(date,low, linestyle='-', color='g', label = 'low')
plt.plot(date,close, linestyle='-', color='r', label = 'close')

plt.legend()
plt.show()