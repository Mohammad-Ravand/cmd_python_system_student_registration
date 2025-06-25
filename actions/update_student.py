from db import cur
from time import time
from utils import clear_previous_input_line
from sqlite3 import IntegrityError
from cmd_colors import bright_cyan,bright_red,bright_green 
from actions.register import get_student_by_email
from utils import get_student_email_input



def update_field(field_name, default_value):
    title = f"Enter student's {bright_red(field_name)} ({default_value}): "
    new_field_value = input(title).strip()

    if new_field_value=='':
        clear_previous_input_line()
        print(f"{bright_red(field_name)} = {bright_green(default_value)}")
    else:
        clear_previous_input_line()
        print(f"{bright_red(field_name)} = {bright_green(new_field_value)}")    
    return default_value if new_field_value == '' else new_field_value

def update_fields_by_user_input(student:dict):
    
    for key,value in student.items():
        if(key=='updated_at'):
            student['updated_at'] = time()
            continue
        if(key in ('id','created_at')): continue
        student[key] = update_field(key,value)
    return student

def update_student_db(student:dict):
    try:
        id,first_name, last_name, age, email, mobile, created_at, updated_at = student.values()
        # Insert the student into the database
        cur.execute("""
            UPDATE students 
                SET first_name=?,
                    last_name=?,
                    age=?,
                    email=?,
                    mobile=?,
                    created_at=?,
                    updated_at=?
                WHERE id=?
        """, (first_name, last_name, age, email, mobile, created_at, updated_at,id))

        # Commit the changes to the database
        cur.connection.commit()
        return True
    except IntegrityError as e:
        print(bright_red("Error updating student: the email already exist."))
        cur.connection.rollback()
        return False

#public function for use in onother modules
def update_student():
    email = get_student_email_input()
    student = get_student_by_email(email)
    if(student is None):
        print(bright_red("student not found."))

    print(bright_cyan("-"*(len(email)+40)))
    updated_fields = update_fields_by_user_input(student)
    updated_student = update_student_db(updated_fields)

    print(bright_cyan("-"*(len(email)+40)))

    if updated_student:
        print(bright_green("Student updated successfully."))
    else:
        print(bright_red("Error: Student was not updated."))



