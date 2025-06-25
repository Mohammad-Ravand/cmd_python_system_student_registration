from actions.register import register_student
from actions.show_student import get_student_infos
from actions.update_student import update_student
from actions.delete_student import delete_student

def get_callback_dict():
    return {
        "1": register_student,
        "2": get_student_infos,
        "3": update_student,
        "4": delete_student
        # Add other command callbacks here
    }
