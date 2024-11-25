grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
end = {}
print(type(end))
students = list(students)
students = sorted(students)

grades2 = [sum(grades[0]) / len(grades[0]),
           sum(grades[1]) / len(grades[1]),
           sum(grades[2]) / len(grades[2]),
           sum(grades[3]) / len(grades[3]),
           sum(grades[4]) / len(grades[4])]
end.update({students[0]: grades2[0],students[1]: grades2[1],students[2]: grades2[2],students[3]: grades2[3],students[4]: grades2[4] })

print(end)