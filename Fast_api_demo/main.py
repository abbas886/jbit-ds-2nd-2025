from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def welcome():
    return "Hello, Welcome to FastAPI Demo Application!"

# how can we acces this api/endpoint.  you should not call by method name
# yous should access this api by using below url
# http://localhost:8000/  # like josn server it run on 3000 port where as FastAPI run on 8000 port

#@app.get("/{name}/{college}")
def greet(name: str, college: str):
    return f"Hello, {name} - {college}! Welcome to FastAPI Demo Application!"


# wanted to do simple crud operations for simle list of integers
#students = [101, 102, 103, 104]


# will test by providing disctionary- with key and value pair   
#@app.post("/students/{student_id}")
#def add_student(student_id: int):
#    students.append(student_id)
#    return {"message": f"Student {student_id} added successfully."}



# wanted to check with proper student data
students = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

#http://localhost:8000/students
@app.get("/students")
def get_all_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": f"Student {student_id} not found."}



@app.post("/students/") 
def add_student(student: dict)-> dict:
    students.append(student)
    return {"message": f"Student {student['id']} added successfully."}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": f"Student {student_id} deleted successfully."}
    return {"message": f"Student {student_id} not found."}







