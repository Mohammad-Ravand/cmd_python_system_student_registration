from actions import get_callback_dict
from tables import create_all_tables
from help import  help_loop
def main():
    create_all_tables()
    help_loop(get_callback_dict())

if __name__ == "__main__":
    main()

