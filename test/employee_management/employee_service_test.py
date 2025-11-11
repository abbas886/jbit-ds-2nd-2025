import employee_service as emp_service

emp_service.initialize()
print("all employees",emp_service.get_all_employees())

print(emp_service.get_employee("emp_001"))

print(emp_service.get_employee("103"))

print("top 2 employees :",emp_service.get_top_n_employees(2))

print("sorded based on salary:",emp_service.sort())


