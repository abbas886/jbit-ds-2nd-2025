#  for explanation purpose - will write code without function
marks =[] # empty list
marks = [45, 67, 89, 23, 78, 90, 56]   # intialize a list
print(marks)

print("first:",marks[0])
print(marks[1])
print(marks[2]) 
print("last element:",marks[-1])

marks.append(100)   # add an element at the end
print(marks)
marks.insert(2, 75)  # insert 75 at index 2
print(marks)
marks.remove(23)   # remove element 23
print(marks)
last_element = marks.pop()   # remove last element
print("removed last element:", last_element)
print("after removing last element",marks)
marks.sort()   # sort the list
print("after sorting:",marks)
marks.sort(reverse=True)  # sort in descending order
print("after sorting in descending order:",marks)

failed_subjects = 0
passed_subjects = 0
marks.append(30)
def sum_of_list_elements(marks):
    total = 0  # local variables - can't access outside function
    global failed_subjects, passed_subjects   ## vriable from outside function
    for sub_marks in marks:    # for element in list
        total += sub_marks
        print("marks : ", sub_marks)
        if sub_marks < 35:
            failed_subjects += 1
        else:
            passed_subjects += 1
    return total,failed_subjects, passed_subjects
total_marks, failed_subjects, passed_subjects = sum_of_list_elements(marks)
print("total marks:", total_marks)
print("failed subjects:", failed_subjects)
print("passed subjects:", passed_subjects)
#print(marks[10])

marks_copy = marks.copy()     # deep copy    -   shallow copy - marks_copy = marks
print("copied list:", marks_copy)
print("original list:", marks)
marks.append(500)
print("after adding 500 to original list",marks)
print("copied list after adding 500 to original list:", marks_copy)
marks_copy.remove(75)
print("after removing 75 from copied list:", marks_copy)
print("original list after removing 75 from copied list:", marks)

#shallow copy example -  both lists will reflect the changes
marks_shallow_copy =  marks   # shallow copy
print("shallow copied list:", marks_shallow_copy)
marks.append(600)
print("after adding 600 to original list",marks)
print("shallow copied list after adding 600 to original list:", marks_shallow_copy)

def update_list(some_list):
    some_list.append(999)
    return some_list

copied_marks = marks.copy()
print("updated list :",update_list(copied_marks))
print("original list after updating copied list:", marks)

# 
marks.append(90)
print(marks.count(90))
marks.remove(90)  # removes first occurrence of 90
print(marks.count(90))
print(marks)

other_list = [10, 20, 30]
#marks.extend(other_list)
other_list.extend(marks)
print("after extending other list:", other_list)
print("index of 78 ", other_list.index(78) )  # returns the index of first occurrence of 78
print("length of other list:", len(other_list))
#sliced_list = other_list[2:10]
marks.clear()
print("after clearing marks list:", marks)

 



