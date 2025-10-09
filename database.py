import sqlite3

# connect to the database
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

print("Database and users table are ready!")

# function to add a new user
def add_user(name, email):
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"User '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print(f"Error: The email '{email}' already exists!")

# ---------------------------
# ✨ Add multiple users at once
users_to_add = [
    ("Omar", "omar@example.com"),
    ("Sara", "sara@example.com"),
    ("Hassan", "hassan@example.com"),
    ("Laila", "laila@example.com"),
]

for name, email in users_to_add:
    add_user(name, email)
# ---------------------------

# close the connection
conn.close()


