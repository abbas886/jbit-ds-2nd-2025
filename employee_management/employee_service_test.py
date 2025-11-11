# test all the methods which are defined in emplloyees_service python file
# we supposed to test using pytest - not discussed.  call the methods

import employee_service  as service

service.initialize()

print("all the employees : " ,service.get_employees("dept1"))   # empty list

print("sorted all the employees based on salary",service.sort())

print("..........")
print("top 2 employees who are geting more salary", service.top_n_employees(3))

print(".....")
print("emp details of 110 - > " , service.get_employee("110"))

emp1 = {
        "emp_id" : "101",
        "emp_name" : "Kavya",
        "emp_salary" : 50000,
        "depart_id" : "dept1"
    }
service.add_employee(emp1)
print(" all the employees after adding new employee")
print(service.get_all_employees())

print("trying to delete emp 101", service.delete_employe("101"))

emp1 = {
        "emp_id" : "101",
        "emp_name" : "Kavya",
        "emp_salary" : 123456,
        "depart_id" : "dept1"
    }
#service.update_employee(emp1)

print("all the employees after updating salary of 101")
print(service.update_employee(emp1))