employees = []


#initialize the employees
def initialize():
    emp1 = {
        "emp_id" : "101",
        "emp_name" : "Kavya",
        "emp_salary" : 50000,
        "depart_id" : "dept1"
    }
    emp2 = {
        "emp_id" : "102",
        "emp_name" : "Harshini",
        "emp_salary" : 60000,
        "depart_id" : "dept2"
    }
    emp3 = {
        "emp_id" : "103",
        "emp_name" : "Abbas",
        "emp_salary" : 70000,
        "depart_id" : "dept3"
    }
    emp4 = {
        "emp_id" : "104",
        "emp_name" : "Ramu",
        "emp_salary" :80000,
        "depart_id" : "dept3"
    }
    employees.append(emp1)
    employees.append(emp2)
    employees.append(emp3)
    employees.append(emp4)

# fetch all the employees
def get_all_employees():
    return employees

# fetch all the employees belongs to particular department
def get_employees(dept_id):
    list = []  # will add employee belongs to the dept_id which is passed
    # iterate the employees and check the field/key with dept_id
    for emp in employees:
        if emp["depart_id"] == dept_id:   # comparing depart_id of all the empllyes
            list.append(emp)    # if it is matching, then only i am adding the list

    return list


#list = [50,100,75,25,300,10]
#print(list)
#list.sort()
#print(list)
#print(list[2:4])
#print(list[3:])
#print(list[:3])

# sort all the employees based on salary field
# sorted(emp_list, key= lambda x : x["salary"],reverse=True)

def sort():
    #employees.sort()  # will not work because it  does not know on which field/key it should sort
    sorted_list = sorted(employees,key = lambda emp : emp["emp_salary"],reverse=True )
    return sorted_list

# top n employees who are getting more salary
def top_n_employees(n):
    # reuse the sort method which we defined above
    sorted_list =  sort()
    return sorted_list[1:n+1]

# add employee, delete employee, update employee

# add employee - first check whether the employee does not exist - add it. 
#  If the employee already exist - return error

def add_employee(emp):
    # will define later
    # first check if the employee with same emp id already exist
   # employees.append(emp)
    if( get_employee(emp["emp_id"]) == -1):  # if the record does not exist
        employees.append(emp)
    return employees


# fetch employee details based on emp id
def get_employee(id):
    for emp in employees:
        if (emp["emp_id"]==id):
            return emp
    return -1  # does not exist

# delete employee
def delete_employe(id):
    # check whether employee exist with the id
    emp = get_employee(id)
    if( emp==-1):  # employee does not exist
        return -1
    employees.remove(emp)
    return "successfully deleted"

# update value of particular employee
def update_employee(emp):
    emp = get_employee(id)
    if( emp==-1):  # employee does not exist
        return -1  # you can't upate
    employees.append(emp) # it will add extra record - again duplicate
    return employees











