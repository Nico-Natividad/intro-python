#dictionary-store data in key-value pairs bracket


student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}
print(student)
print(student["name"])
print(student.get("age"))

student["age"] = 21
print(student)
#check if item is in dictionary
if "major" in student:
    print("Major is present in the dictionary.")


students = {
    "student1": {       
        
        "name": "Alice",
        "age": 22,
        "major": "Mathematics"
    },
    "student2": {
        "name": "Bob",
        "age": 23,
        "major": "Physics"
    }
}
#accessnested value
print(students["student1"]["major"])
print(students["student2"]["major"])



