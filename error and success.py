import cgi
import sqlite3

# Get form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Connect to SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Check if the user exists and the password is correct
cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
user = cursor.fetchone()

# Generate HTML response
print("Content-type: text/html\n")
if user:
    with open('success.html', 'r') as file:
        print(file.read())
else:
    with open('error.html', 'r') as file:
        print(file.read())

# Close the connection
conn.close()
