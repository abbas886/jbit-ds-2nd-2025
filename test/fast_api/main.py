from fastapi   import FastAPI

app = FastAPI()

students = [
    {"id": 101, "name": "Alice", "age": 21},

    {"id": 102,"name": "Bob", "age": 22},
    {"id": 103,"name": "Charlie", "age": 23}
    ]

@app.get("/" )
def hello_world() -> str:
    return "Hello, World!"

@app.get("/{name}")
def read_item(name) -> dict:
    return ({"name": name} )

@app.get("/students/")
def get_students() -> list:
    return students
@app.get("/students/{student_id}")
def get_student(student_id: int) -> dict:
    for student in students:
        if student["id"] == student_id:
            return student
    return {"error": "Student not found"}

@app.post("/students/")
def create_student(student: dict) -> dict:
    students.append(student)
    return student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: dict) -> dict:
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}   
@app.delete("/students/{student_id}")
def delete_student(student_id: int) -> dict:
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)
            return deleted_student
    return {"error": "Student not found"}   