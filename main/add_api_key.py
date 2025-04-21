import sqlite3
import secrets

# Step 1: Create or connect to a SQLite database
db_name = "api_database.db"  # SQLite database file name
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Step 2: Create a table for storing API keys
cursor.execute('''
CREATE TABLE IF NOT EXISTS api_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    api_key TEXT NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
print("Table 'api_keys' created or already exists.")

# Step 3: Generate a secure API key and add it to the database
def generate_api_key():
    return secrets.token_hex(32)  # Generates a 64-character secure token

new_api_key = generate_api_key()
cursor.execute("INSERT INTO api_keys (api_key) VALUES (?)", (new_api_key,))
conn.commit()  # Save changes
print(f"New API key added: {new_api_key}")

# Step 4: Fetch and display all API keys in the database
cursor.execute("SELECT * FROM api_keys")
rows = cursor.fetchall()
print("All API keys in the database:")
for row in rows:
    print(row)

# Step 5: Close the database connection
conn.close()
print("Database connection closed.")
