#  Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# The code snippet gives the output shown in the following screenshot: 
import matplotlib.pyplot as plt
import numpy as np

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
userList = [12342, 12112, 123, 12356, 12, 2321]

#setting up width
x = np.arange(len(languages))

plt.bar(languages,popularity, color='b', width=0.25, label='Programming Language Popularity')
plt.bar(languages,userList, color='g', width=0.5, label='Programming Language Popularity')
plt.legend()
plt.show()

