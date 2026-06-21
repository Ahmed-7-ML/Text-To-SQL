import sqlite3

# Connect to DB
conn = sqlite3.connect("Faculty.db")

# Create a Cursor
cursor = conn.cursor()

# Clean up old tables (the order is important: we clean up the Secondary(Marks) first and then the Primary(Students) to prevent constraints problems)
cursor.execute("DROP TABLE IF EXISTS Marks;")
cursor.execute("DROP TABLE IF EXISTS Students;")
cursor.execute("DROP TABLE IF EXISTS Users;")

# Create Students Table
students_table_schema = """
CREATE TABLE IF NOT EXISTS Students(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(25) UNIQUE,
    DoB TEXT,
    Section INTEGER
);
"""

marks_table_schema = """
CREATE TABLE IF NOT EXISTS Marks(
    MarkId INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentId INTEGER,
    Subject VARCHAR(50),
    Score INTEGER,
    FOREIGN KEY(StudentId) REFERENCES Students(Id)
);
"""

users_table_schema = """
CREATE TABLE IF NOT EXISTS Users(
    Username VARCHAR(50) PRIMARY KEY,
    Password VARCHAR(50) NOT NULL,      -- Must be Hashed
    Role     VARCHAR(25) NOT NULL
)
"""

# Execution Order is also Important as Marks Table refer to Students Table
cursor.execute(students_table_schema)
cursor.execute(marks_table_schema)
cursor.execute(users_table_schema)

# Insert some student records
students_insert_records = [
    "INSERT OR IGNORE INTO Students (Name, DoB, Section) VALUES('Ahmed Akram', '18-06-2003', 2)",           # ID = 1
    "INSERT OR IGNORE INTO Students (Name, DoB, Section) VALUES('Aya Amer', '20-04-2002', 1)",              # ID = 2
    "INSERT OR IGNORE INTO Students (Name, DoB, Section) VALUES('Shimaa Mohamed', '21-02-2006', 3)",        # ID = 3
    "INSERT OR IGNORE INTO Students (Name, DoB, Section) VALUES('Zeyad Akram', '31-3-2001', 1)",            # ID = 4
    "INSERT OR IGNORE INTO Students (Name, DoB, Section) VALUES('Ibrahim Diaz', '28-02-2004', 5)"           # ID = 5
]

marks_insert_records = [
    # Ahmed Akram
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (1, 'Machine Learning', 90)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (1, 'Introduction to AI', 99)",
    
    # Aya Amer
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (2, 'Deep Learning', 80)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (2, 'Operating Systems', 85)",
    
    # Shimaa Mohamed
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (3, 'Python Programming', 90)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (3, 'Large Language Models', 70)",
    
    # Zeyad Akram
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (4, 'RAG & Agentic AI', 90)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (4, 'Machine Learning', 80)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (4, 'Deep Learning', 60)",
    
    # Ibrahim Diaz
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (5, 'Python Programming', 90)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (5, 'Machine Learning', 90)",
    "INSERT OR IGNORE INTO Marks (StudentId, Subject, Score) VALUES (5, 'Operating Systems', 90)",    
]

users_insert_records =  [
    "INSERT OR IGNORE INTO Users VALUES ('ahmed_admin', 'ahmed123', 'admin')",
    "INSERT OR IGNORE INTO Users VALUES ('omar_207', 'omar100', 'user')",
    "INSERT OR IGNORE INTO Users VALUES ('cr7_100', 'cris_07', 'user')"
]

for record in students_insert_records:
    cursor.execute(record)

for record in marks_insert_records:
    cursor.execute(record)

for record in users_insert_records:
    cursor.execute(record)

# Display all Records
print("Inserted Users:")
data = cursor.execute("""SELECT * FROM Users""")

for row in data:
    print(row)

print("_"*50)

print("Inserted Students:")
data = cursor.execute("""SELECT * FROM Students""")

for row in data:
    print(row)

print("_"*50)

print("Inserted Marks:")
data = cursor.execute("""SELECT * FROM Marks""")

for row in data:
    print(row)

print("_"*50)

print("📊 Displaying Joined Records (Verification):")
query = """
        SELECT Students.Name, Students.Section, Marks.Subject, Marks.Score 
        FROM Students JOIN Marks 
        ON Students.Id = Marks.StudentId;
"""
data = cursor.execute(query)

for row in data:
    print(row)

# Commit & Close the Connection
conn.commit()
conn.close()
print("\n✅ Database updated successfully with Multi-Table Schema!")
