import sqlite3

# Step 1: Connect to (or create) the database file
conn = sqlite3.connect('users.db')

# Step 2: Create a cursor to interact with the database
c = conn.cursor()

# Step 3: Create a table named 'users' if it doesn't exist already
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Step 4: Save (commit) the changes and close the connection
conn.commit()
conn.close()

print("✅ Database and table created successfully!")
