# crud operations for both employee and department and expose the mothods outside
# Employee operations
import employee as emp
import department as dept



# initialize departments
def init_departments():
    dept.add_department(1,"CSE")
    dept.add_department(2,"ECE")
    dept.add_department(3,"EEE")


def init_employees():
    emp.add_employee(1, 'Alice', 'Developer',1)
    emp.add_employee(2, 'Bob', 'Designer',2)

def get_employees():
    emp_list = emp.get_all_emplolyees()
    print(emp_list)
def get_all_employees(dept_id):
    emp_list = emp.get_all_employees(dept_id)
    print("emmployees belongs to department:",dept_id)
    print(emp_list)



init_departments()
init_employees()
get_employees()
get_all_employees(1)










