# define crud operations for employee

emp_list=[]

def initialize():
    emp1={
        "id":"101",
        "name": "emp1",
        "salary": 45000,
        "dept_id": "dept_101"
    }
    emp2={
        "id":"102",
        "name": "emp2",
        "salary": 55000,
        "dept_id": "dept_102"
    }

    emp3={
        "id":"103",
        "name": "emp3",
        "salary": 60000,
        "dept_id": "dept_101"
    }
    emp_list.append(emp1)
    emp_list.append(emp2)
    emp_list.append(emp3)
    return emp_list



def get_all_employees():
    return emp_list

def get_employee(id):
    for emp in emp_list:
        if(emp["id"]==id):
            return emp
    return -1

def get_employees(dept_id):
    list = []
    for emp in emp_list:
        if(emp["dept_id"]==dept_id):
            list.append(emp)
    return list

def get_top_n_employees(n):
    sorted_list = sorted(emp_list, key= lambda x : x["salary"])
    return sorted_list[n:]

def sort():
    sorted_list = sorted(emp_list, key= lambda x : x["salary"],reverse=True)
    return sorted_list


