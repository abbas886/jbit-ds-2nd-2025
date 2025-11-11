# department crud operations without class
departments = []  # empty list to hold department records

def add_department(dept_id, name):
    department = {
        'id': dept_id,
        'name': name
    }
    departments.append(department)
    print(f"Department {name} added.")
def view_departments():
    if not departments:
        print("No departments to display.")
        return
    for dept in departments:
        print(f"ID: {dept['id']}, Name: {dept['name']}")
def update_department(dept_id, name=None):
    for dept in departments:
        if dept['id'] == dept_id:
            if name:
                dept['name'] = name
            print(f"Department ID {dept_id} updated.")
            return
    print(f"Department ID {dept_id} not found.")
def delete_department(dept_id):
    global departments
    departments = [dept for dept in departments if dept['id'] != dept_id]
    print(f"Department ID {dept_id} deleted if existed.")
# Example usage
# add_department(1, 'Human Resources')
#add_department(2, 'Finance')
#view_departments()  
#update_department(1, name='HR')
#view_departments()
#delete_department(2)
#view_departments()
