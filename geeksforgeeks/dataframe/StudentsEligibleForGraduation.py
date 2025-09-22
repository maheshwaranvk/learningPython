#https://www.geeksforgeeks.org/problems/students-eligible-for-graduation/1

import pandas as pd

studentData = [
    [101, 'Alice', 2025, 130, 32],
    [102, 'Bob', 2024, 110, 28],
    [103, 'Charlie', 2025, 120, 30],
    [104, 'David', 2023, 140, 40]
]

studentDataDF = pd.DataFrame(studentData, columns=['student_id','student_name','graduation_year','total_credits','completed_courses'])

print(studentDataDF)
print(studentDataDF[(studentDataDF['total_credits']>=120) & (studentDataDF['completed_courses']>=30)])