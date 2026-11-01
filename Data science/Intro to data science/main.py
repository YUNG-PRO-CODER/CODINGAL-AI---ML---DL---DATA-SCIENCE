import numpy as np

details = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('James', 9, 166.6), ('John', 10, 155), ('Ram', 12, 188.85)]

students = np.array(student_details, dtype=details)
print(students)
n = np.sort(students, order='height')
print(n)