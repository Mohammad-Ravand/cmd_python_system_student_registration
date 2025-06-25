from cmd_colors import bright_red,bright_green
from utils import clear_previous_input_line
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

   
if __name__ == "__main__":
    update_field("first_name", "John")
    update_field("last_name", "Doe")
    # print(type(test_fetch_student("