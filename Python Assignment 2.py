age_list = [24, 25, 26, 27, 28]
print(age_list)

name_list = ["Anu", "Bala", "Charu", "Divya", "Esha"]
print(name_list)

name_list.append("Yazhini")
print(name_list)

age_list.insert(2, 30)
print(age_list)

name_list.remove("Yazhini")
print(name_list)

age_list.pop()
print(age_list)

age_list.extend([29, 30, 26])
print(age_list)

age_list.sort(reverse=True)
print(age_list)

print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))

print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])

student_marks = {
    "Anu": 85,
    "Bala": 90,
    "Charu": 78,
    "Divya": 88,
    "Esha": 95
}

print(student_marks)

print("Anu's mark:", student_marks["Anu"])

student_marks["Janani"] = 80
print(student_marks)

student_marks["Charu"] = 82
print(student_marks)

print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Items:", student_marks.items())

my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print(my_set)


try:
    my_set[4] = 's'

except TypeError:
    print("Error: Sets do not support item assignment.")

    set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# Performance Category Program

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent performance! Keep it up.")

elif score >= 4:
    print("Average: Good effort! Keep practicing.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")