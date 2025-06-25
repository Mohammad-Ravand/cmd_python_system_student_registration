from cmd_colors import green,bright_magenta,orange_bold,light_gray,bright_blue,bright_red
def show_help():
    print("\033[38;5;208m\033[1m")  # Set orange color and bold (larger font not possible in terminal)
    print(f"{orange_bold("WELCOME TO THE STUDENT REGISTRATION SYSTEM!".center(70))}")
    print(" \033[0m")  # Reset formatting  print("Here are the available commands:")
    print(f" {green(1)}. {light_gray("register_student - Register a new student.")}")
    print(f" {green(2)}. {light_gray("view_students - View all registered students.")}")
    print(f" {green(3)}. {light_gray("update_student - Update an existing student's information.")}")
    print(f" {green(4)}. {light_gray("delete_student - Delete a student from the system.")}")
    print(f" {green(5)}. {light_gray("exit - Exit the system.")}")
    print(f" {green(6)}. {light_gray("help - Show this help message.")}")  # Light crimson (bright red)
    print(f" {bright_magenta("To use a command, simply type the command number and follow the prompts (like 1 or 2 ...).")}")

def get_help_number()->int:
    help_number = input(bright_magenta("Enter the command number you need help with (or press Enter to skip): ")).strip()
    print(f"{bright_blue("You entered:")}", green(help_number))
    
    return help_number if help_number else None

def help_loop(callback_dict:dict)->None:
    show_help()

    while((help_number :=get_help_number()) is not None):
        if help_number in callback_dict:
            callback_dict[help_number]()
        elif help_number in ("5","exit"):
            print("Exiting help. Goodbye!")
            break
        elif help_number == "6":
            show_help()
        else:
            print(bright_red("Invalid command number. Please try again."))