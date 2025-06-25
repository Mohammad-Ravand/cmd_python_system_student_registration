from db import cur


def create_student_table():
    # create table students
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name varchar(50),
        last_name varchar(50),
        age INTEGER,
        email varchar(100) unique,
        mobile varchar(15),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create trigger to update 'updated_at' on row update
    cur.execute("""
    CREATE TRIGGER IF NOT EXISTS update_students_updated_at
    AFTER UPDATE ON students
    FOR EACH ROW
    BEGIN
        UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
    END;
    """)
