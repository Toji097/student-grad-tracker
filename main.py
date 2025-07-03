#Okay first lets start by setting a function that will take output the grades for the user/students

def student_grades(student_percentage):

    if student_percentage >= 90:
        return "A+"
    elif student_percentage >= 80:
        return "A"
    elif student_percentage >= 70:
        return "B"
    elif student_percentage >= 60:
        return "C"
    elif student_percentage >= 50:
        return "D"
    else:
        return "Fail"
    

#Okay lets take some input from the user

name = input("Please enter your name: ")
num_of_subjects = int(input("How many subjects did you take? "))

marks = []
for i in range(num_of_subjects):
    mark = float(input(f"Enter the marks for Subject {i+1}: " ))
    marks.append(mark)


total = sum(marks)
average = total / num_of_subjects
percentage = (total / (num_of_subjects * 100)) * 100
grade = student_grades(percentage)


print(f"\nName: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
