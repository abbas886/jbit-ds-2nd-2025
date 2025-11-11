# declare disctionary
student = {
    "student_id" :  "csc_101",
    "student_name" : "harshini",
    "branch" :  "cse"

}
print(student)
print (student.get("student_name") )   # studnet["student_name"]
print("name of the student of csc_101", student["student_name"])
print("fields names i.e, keys:",student.keys)
print(student.values)
# loop/iterate student distionary

#student.keys - fetch only fields/properties
# student.values - only values belongs to the keys
# student.items - fetch both key and value
for key, value in student.items():
    print(f"{key} -> {value}")

# add different student objects in the "list" and do certain opertations
student1 = {
    "student_id" :  "csc_101",
    "student_name" : "harshini",
    "branch" :  "cse",
    "marks" : 450
}
student3 = {
    "student_id" :  "csc_102",
    "student_name" : "Kishore",
    "branch" :  "cse",
    "marks" : 500
}
student2 = {
    "student_id" :  "csc_103",
    "student_name" : "Ram",
    "branch" :  "ece",
    "marks" : 600
}

students =[]
students.append(student1)
students.append(student2)
students.append(student3)

print(students)

# using methods
def get_all_students():
    return students

print("search oerations...")
# get details of particular student based on id
def get_student_details(student_id):
    # search - linear search
    for student in students:   # fetch student details one by one
        if (student["student_id"] == student_id):
            return student
    return f"no student exist with id {student_id}"


# test


print(get_student_details("csc_110"))

# want to acces only marks of particular student
def get_student_marks(student_id):
     for student in students:   # fetch student details one by one
        if (student["student_id"] == student_id):
            return student_id,student["marks"]     # instead of returning all the data, fetch only particular field
     return "student does not exist"
# test - call the method
print( get_student_marks("csc_103"))


list1 = [10,20,50,30]

# list.remove("csc_103")  # it should not work
print(" student details before remove")
print(students)

students.remove(student1)
students.remove(student2)
students.remove(student3)

print(" student details after remove")
print(students)

# tomorrow - all major search and crud(create, retrieve,update, delete) operations of student/employee/player
# define proper methods to do above operations
# add_student,  delete_student, update_details, search for particular students
# aggretate operations - sum, min, max, average, count
# employee and department/branch
