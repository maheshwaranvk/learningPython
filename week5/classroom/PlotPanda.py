import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv')
print(df)

df.plot.line(color=['blue','brown','green','red'], marker="*", linestyle='-')
df.plot.bar(x='Day',color=['blue','brown','green','red'], edgecolor='Green')
df.plot.hist(x='Day',bins = 5, color=['blue','brown','green','red'], edgecolor='Green', alpha=0.5)

df1 = pd.DataFrame({'Module':['AI', 'ML', 'Python', 'DataStructures'], 'Teamsize':[135, 125, 125, 115] })
df1.set_index('Module', inplace=True)
df1.plot.pie(y='Teamsize',color=['blue','brown','green','red'], autopct='%1.1f%%' )

plt.show()