import matplotlib.pyplot as plt

severity = ["High","Medium","Low"]
defectCounts = [10,15,5]

plt.pie(defectCounts, labels=severity, autopct="%1.1f%%", startangle=90)
plt.show()