from actions.register import get_student_by_email
from cmd_colors import bright_red,bright_blue,bright_green,bright_cyan,light_gray,bright_green_start,bright_green_end


#public function
def get_student_infos():
    print(light_gray("Enter student's email:"), end='')

    print(bright_green_start(),end='')
    email = input("")
    print(bright_green_end(),end='')
    studnet = get_student_by_email(email)
    print(bright_cyan("-"*(len(email)+40)))
    if studnet:
        print(f"{bright_blue("Student ID")}: {bright_green(studnet['id'])}")
        print(f"{bright_blue("First Name")}: {bright_green(studnet['first_name'])}")
        print(f"{bright_blue("Last Name")}: {bright_green(studnet['last_name'])}")
        print(f"{bright_blue("Age")}: {bright_green(studnet['age'])}")
        print(f"{bright_blue("Email")}: {bright_green(studnet['email'])}")
        print(f"{bright_blue("Mobile")}: {bright_green(studnet['mobile'])}")
        print(f"{bright_blue("Created At")}: {bright_green(studnet['created_at'])}")
        print(f"{bright_blue("Updated At")}: {bright_green(studnet['updated_at'])}")
    else:
        print(bright_red("No student found with that email."))