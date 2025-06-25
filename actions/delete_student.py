from actions.register import get_student_by_email
from cmd_colors import bright_red,bright_yellow,bright_green
from utils import get_student_email_input
from db import cur


def delete_student_db(id:str):
    try:
        # Delete the student from the database
        cur.execute("DELETE FROM students WHERE id = ?", (id,))
        cur.connection.commit()
        return True
    except Exception as e:
        print(bright_red(f"Error deleting student: {e}"))
        cur.connection.rollback()
        return False

def get_confirmation():
    confirmation = input("Are you sure you want to delete this student? (yes/no): ").strip().lower()
    return confirmation == 'yes'

def delete_student():
    email = get_student_email_input()
    student = get_student_by_email(email)
    if(student is None):
        print(bright_red("student not found."))
    
    else:
        if not get_confirmation():
            print(bright_yellow("Deletion cancelled."))
            return
        deleted_student = delete_student_db(student['id'])
        if deleted_student:
            print(bright_green(f"Student with email {email} has been successfully deleted."))
        else:
            print(bright_red("Failed to delete the student."))