import json
import os
from enum import Enum


class Choice(Enum):
    SHOW = 1
    ADD = 2
    REMOVE = 3
    UPDATE = 4
    EXIT = 5

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["age"])

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Student.from_dict(student) for student in data]
        return []

    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump([student.to_dict() for student in self.students], f, indent=4)

    def add_student(self, id, name, age):
        student = Student(id, name, age)
        self.students.append(student)
        self.save_students()

    def remove_student(self, id):
        self.students = [s for s in self.students if s.id != id]
        self.save_students()

    def update_student(self, id, name=None, age=None):
        for student in self.students:
            if student.id == id:
                if name:
                    student.name = name
                if age:
                    student.age = age
                self.save_students()
                break

    def show_students(self):
        if not self.students:
            print("No students found.")
        for student in self.students:
            print(student)

def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print(f"{Choice.SHOW.value}. Show Students")
        print(f"{Choice.ADD.value}. Add Student")
        print(f"{Choice.REMOVE.value}. Remove Student")
        print(f"{Choice.UPDATE.value}. Update Student")
        print(f"{Choice.EXIT.value}. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice not in [Choice.SHOW.value, Choice.ADD.value, Choice.REMOVE.value, Choice.UPDATE.value, Choice.EXIT.value]:
                print("Invalid choice, please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == Choice.SHOW.value:
            manager.show_students()
        elif choice == Choice.ADD.value:
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            manager.add_student(id, name, int(age))
            print("Student added successfully!")
        elif choice == Choice.REMOVE.value:
            id = input("Enter student ID to remove: ")
            manager.remove_student(id)
            print("Student removed successfully!")
        elif choice == Choice.UPDATE.value:
            id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            manager.update_student(
                id, name if name else None, int(age) if age else None
            )
            print("Student updated successfully!")
        elif choice == Choice.EXIT.value:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
