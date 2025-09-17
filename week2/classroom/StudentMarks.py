marks = [78, 85, 62, 90, 55, 88]
distinctionMarks = []
print("Highest Mark : ",max(marks))
print("Lowest Mark : ",min(marks))
print("Average Mark : ", sum(marks)/len(marks))
for i in range(len(marks)):
    if marks[i] >75:
        print("Distinction Marks : ",marks[i])
        distinctionMarks.append(marks[i])
marks.remove(55)
print(marks)
marks.sort()
print("Sorted Marks : ",marks)
print("Distinction Marks : ", distinctionMarks)