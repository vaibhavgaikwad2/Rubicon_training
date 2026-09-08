import sqlite3

connection = sqlite3.connect("college.db")

cursor = connection.cursor()

print("\nDatabase connected successfully!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (

    id INTEGER PRIMARY KEY,

    name TEXT NOT NULL,

    marks REAL,

    department TEXT
)
""")

connection.commit()

print("Students table created!")

students = [

    (1, "Amit", 82, "Computer"),

    (2, "Neha", 91, "Computer"),

    (3, "Rahul", 74, "IT"),

    (4, "Pooja", 88, "IT"),

    (5, "Kiran", 95, "Computer")
]

cursor.executemany(
    """
    INSERT OR IGNORE INTO students
    (id, name, marks, department)

    VALUES (?, ?, ?, ?)
    """,

    students
)

connection.commit()

print("Students inserted!")

print("\n--- ALL STUDENTS ---")

cursor.execute(
    "SELECT * FROM students"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("\n--- MARKS >= 80 ---")

cursor.execute(
    """
    SELECT name, marks
    FROM students
    WHERE marks >= ?
    """,

    (80,)
)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("\n--- SORTED BY MARKS ---")

cursor.execute(
    """
    SELECT name, marks
    FROM students
    ORDER BY marks DESC
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row)


print("\n--- FIND STUDENT ID 2 ---")

cursor.execute(
    """
    SELECT *
    FROM students
    WHERE id = ?
    """,

    (2,)
)

student = cursor.fetchone()

if student:

    print("Student Found:", student)

else:

    print("Student Not Found")


print("\n--- UPDATE ---")

cursor.execute(
    """
    UPDATE students

    SET marks = ?

    WHERE id = ?
    """,

    (96, 1)
)

connection.commit()

print("Amit's marks updated!")


cursor.execute(
    """
    SELECT *
    FROM students
    WHERE id = ?
    """,

    (1,)
)

print(cursor.fetchone())


print("\n--- DELETE ---")

cursor.execute(
    """
    DELETE FROM students

    WHERE id = ?
    """,

    (3,)
)

connection.commit()

print("Student ID 3 deleted!")


print("\n--- FINAL DATA ---")

cursor.execute(
    "SELECT * FROM students"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

print("\n--- TRANSACTION TEST ---")

try:

    cursor.execute(
        """
        UPDATE students

        SET marks = ?

        WHERE id = ?
        """,

        (100, 2)
    )

    connection.commit()

    print("Transaction successful!")

except sqlite3.Error as error:

    connection.rollback()

    print("Database Error:", error)


print("\n--- FINAL STUDENT RECORDS ---")

cursor.execute(
    """
    SELECT *
    FROM students
    ORDER BY marks DESC
    """
)

for row in cursor.fetchall():

    print(
        "ID:", row[0],
        "| Name:", row[1],
        "| Marks:", row[2],
        "| Department:", row[3]
    )


connection.close()

print("\nDatabase connection closed!")

print("=" * 60)
print("             PROGRAM COMPLETED")
print("=" * 60)