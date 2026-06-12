import sqlite3
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
   )
   """)
    conn.commit()
    conn.close()

def insert_student(name, marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
    conn.commit()
    conn.close()
    print("student inserted successfully")
    
def get_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\nAll Students:")
        print("-"*40)
        for row in rows:
            print(f"id: {row[0]}, name: {row[1]}, marks: {row[2]}")
    else:
        print("No students found")
    conn.close()

def get_student_by_id(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT*FROM students WHERE id = ?",
        (student_id,)
    )
    row = cursor.fetchone()
    if row:
        print(f"id: {row[0]}, name: {row[1]}, marks: {row[2]}")
    else:
        print("students not found")
        conn.close()

def update_marks(student_id, new_marks):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET marks = ? WHERE  id = ?",
        (new_marks, student_id)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("marks updated successfully")
    else:
        print("students not found")
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()

def get_students_above(threshold):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT*FROM students WHERE marks > ?",
        (threshold, )
    )
    rows = cursor.fetchall()
    print(f"\nstudents with marks above{threshold}:")
    print("-"*40)
    if rows:
        for row in rows:
            print(f"id: {row[0]}, name: {row[1]}, marks: {row[2]}")
    else:
        print("no students found")
    conn.close()

def main():
    create_table()
    while True:
        print("\n========STUDENT DATABASE SYSTEM========")
        print("1. insert student")
        print("2. view all students")
        print("3. get student by IDs")
        print("4. update marks")
        print("5. delete student")
        print("6. students above threshold")
        print("7. exit")
        choice = input("enter you choice:")
        if choice == "1":
            name = input("enter student name: ")
            marks = int(input("enter marks: "))
            insert_student(name, marks)
        elif choice == "2":
            get_all_students()
        elif choice == "3":
            student_id = int(input("enter student ID: "))
            get_student_by_id(student_id)
        elif choice == "4":
            student_id = int(input("enter student ID: "))
            new_marks = int(input("enter new marks: "))
            update_marks(student_id, new_marks)
        elif choice == "5":
            student_id = int(input("enter student ID: "))
            delete_student(student_id)
        elif choice == "6":  
            threshold = int(input("enter threshold marks: "))
            get_students_above(threshold)
        elif choice == "7":
            print("exiting program...")
            break
        else:
            print("invalid choice. please try again")

main()