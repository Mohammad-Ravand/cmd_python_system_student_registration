# Student Management System (Python, SQLite)

A command-line application for managing student records using Python and SQLite. This project allows users to register, update, view, and delete student information efficiently, with a focus on modularity and code clarity.

## Features

- **Register Students:** Add new students with unique email addresses.
- **View Students:** Display all registered students or search by email.
- **Update Students:** Modify existing student details.
- **Delete Students:** Remove students from the database with confirmation.
- **Colorful CLI Output:** Enhanced user experience with colored messages.
- **Persistent Storage:** Uses SQLite for reliable data management.

## Project Structure

```
actions/
    actions.py
    delete_student.py
    register.py
    show_student.py
    update_student.py
cmd_colors.py
db.py
help.py
main.py
test.py
utils.py
tables/
    create_tables.py
    students.py
database.db
pyproject.toml
README.md
```

- `main.py`: Entry point for the CLI application.
- `actions/`: Contains modules for CRUD operations.
- `tables/`: Database schema and table creation scripts.
- `db.py`: Database connection and cursor setup.
- `cmd_colors.py`: Utility for colored terminal output.
- `utils.py`: Helper functions for input and validation.
- `help.py`: CLI help and usage instructions.
- `test.py`: Test cases for core functionalities.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (for dependency management)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/learning-python.git
   cd learning-python
   ```

2. **Install dependencies using uv:**
   ```sh
   uv pip install -r requirements.txt
   ```
   Or, if using `pyproject.toml`:
   ```sh
   uv pip install -r pyproject.toml
   ```
   *(If `requirements.txt` is not present, use `uv` with `pyproject.toml`.)*

3. **Initialize the database:**
   ```sh
   uv run tables/create_tables.py
   ```

### Usage

Run the main application:

```sh
uv run main.py
```

Follow the on-screen prompts to register, view, update, or delete students.

### Running Tests

```sh
uv run test.py
```

## Customization

- Modify `cmd_colors.py` to change CLI color schemes.
- Update `tables/students.py` to adjust the student schema.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License.
