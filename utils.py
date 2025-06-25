from cmd_colors import bright_green_start, bright_green_end, light_gray

def to_dict(row):
    if row is not None:
        # Get column names from cursor description
        columns = [desc[0] for desc in cur.description]
        
        inserted_user = dict(zip(columns, row))
    else:
        inserted_user = None
    return inserted_user


def clear_previous_input_line():
    """
    Clears the previous input line in the terminal.
    This is useful for overwriting input prompts.
    """
    print('\033[F\033[K', end='')  # Move cursor up one line and clear the line


def get_student_email_input():
    print(light_gray("Enter student's email:"), end='')

    print(bright_green_start(),end='')
    email = input("")
    print(bright_green_end(),end='')
    
    return email

