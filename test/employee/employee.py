# implement crud operations for employee records without class
employees = []  # empty list to hold employee records
def add_employee(emp_id, name, position,department_id=None):
    employee = {
        'id': emp_id,
        'name': name,
        'position': position,
        'department_id': department_id
    }
    employees.append(employee)
    print(f"Employee {name} added.")
def view_employees():
    if not employees:
        print("No employees to display.")
        return
    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}")

def get_all_emplolyees():
        return employees

# return all the employees belongs to particular department
def get_all_employees(dept_id):
        emp_list = []
        for emp in employees:
             if emp.get("department_id") == dept_id:
                emp_list.append(emp)
        return emp_list

def update_employee(emp_id, name=None, position=None,department_id=None):
    for emp in employees:
        if emp['id'] == emp_id:
            if name:
                emp['name'] = name
            if position:
                emp['position'] = position
            if department_id:
                emp['department_id'] = department_id
            print(f"Employee ID {emp_id} updated.")
            return
    print(f"Employee ID {emp_id} not found.")
def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp['id'] != emp_id]
    print(f"Employee ID {emp_id} deleted if existed.")


# Example usage
add_employee(1, 'Alice', 'Developer')
add_employee(2, 'Bob', 'Designer')
view_employees()
update_employee(1, position='Senior Developer')
view_employees()
delete_employee(2)
view_employees()
