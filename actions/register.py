from time import time
from db import cur
from sqlite3 import IntegrityError
from cmd_colors import bright_red,red,bright_magenta,cyan,bright_cyan


# 1 -  get user infos
# 2 - insert data into database
# 3 - get user from  database
# 4 - print the result of register user confirmation

def insert_student(first_name, last_name, age, email, mobile)->bool:
    created_at = time()  # Use current timestamp for created_at
    updated_at = time()

    try:
        # Insert the student into the database
        cur.execute("""
            INSERT INTO students (first_name, last_name, age, email, mobile, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, age, email, mobile, created_at, updated_at))

        # Commit the changes to the database
        cur.connection.commit()
        return True
    except IntegrityError as e:
        print(bright_red("Error inserting student: the email already exist."))
        cur.connection.rollback()
        return False

def get_student_by_email(email):
    # Fetch the inserted user by email (assuming email is unique)
    cur.execute("SELECT * FROM students WHERE email = ?", (email,))
    row = cur.fetchone()
    
    if row is not None:
        # Get column names from cursor description
        columns = [desc[0] for desc in cur.description]
        return dict(zip(columns, row))
    else:
        return None
    
def print_registration_confirmation(student):
    if student:
        print(bright_magenta(f"Student {bright_cyan('#')+cyan(student['id'])} first_name={cyan(student['first_name'])} last_name={cyan(student['last_name'])} registered successfully."))
    else:
        print(bright_red("Registration failed. Student not found."))

def get_student_input(*args,**kwargs):
    
    first_name = input(f"Enter student's {bright_red("first_name")}: ")
    last_name = input(f"Enter student's {bright_red("last_name")}: ")
    age = input(f"Enter student's {bright_red("age")}: ")
    email = input(f"Enter student's {bright_red("email")}: ")
    mobile = input(f"Enter student's {bright_red("mobile")}: ")
    
    return first_name, last_name, age, email, mobile

#public function to register a student
def register_student():
    first_name ,last_name ,age,email,mobile = get_student_input()

    # Insert the student into the database
    inserted = insert_student(first_name, last_name, age, email, mobile)
    if not inserted:
        print("\033[91mFailed to register student. Please try again.\033[0m")
        return
    # Fetch the inserted user by email (assuming email is unique)
    inserted_user = get_student_by_email(email)

    # Print the registration confirmation
    print_registration_confirmation(inserted_user)


