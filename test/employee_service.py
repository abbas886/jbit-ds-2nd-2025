# create rest api for employee

import requests
import json


base_url="http://localhost:3000/"
def get_all_employees():
    resp = requests.get(base_url+"/employees")
    return resp.json()

def get_employee(id):
    resp = requests.get(f"{base_url}/employees?id={id}")
    print(f"employee details of {id}", resp.json())
    return resp.json()

def add_employee(id,name,department):
    if(get_employee(id)!=""):
        return (f"employ already exist with emp id {id}")

    emp = {
        "id": id,
        "name": name,
        "department":department
    }
    resp = requests.post(f"{base_url}/employees/",json=emp)
    print("after adding new record",resp.json())
    return resp

def update_employee(id,name,department):
    emp = {
        "id": id,
        "name": name,
        "department":department
    }
    resp = requests.put(base_url+"/employees",json=emp)
    print("after adding new record",resp.json())
    return resp

def delete_employee(id):
     if(get_employee(id)==""):
        return (f"employ does not  exist with emp id {id}")
     resp =  requests.delete(f"{base_url}/employees/{id}")
     return resp


print("all emploees : ", get_all_employees())
add_employee(101,"Santhosh", "Civil")
add_employee(101,"Santhosh", "Civil")
add_employee(101,"Santhosh", "Civil")
print("all emploees after adding 101 : ", get_all_employees())
#update_employee(101,"Santhosh","Mechanical")

print(get_employee(1))

print(delete_employee(1))

print(f"employees after deleting id 1:", get_all_employees())


