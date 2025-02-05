import sqlite3

def folder_path(path):
    conn = sqlite3.connect('database.db') # connecting to the database file
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Path (path text)")
    conn.commit()
    c.execute("INSERT INTO Path (path) VALUES (?)", (path,))
    conn.commit()

    conn.close()

def check_folder_path():
    conn = sqlite3.connect('database.db') # connecting to the database file
    c = conn.cursor()

    # Check if the table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Path';")
    
    if c.fetchone():  # Table exists
        c.execute("SELECT path FROM Path ORDER BY ROWID DESC LIMIT 1;")
        result = c.fetchone()
        conn.close()
        return result[0] if result else None  # Return the path if it exists
    else:  # Table does not exist
        conn.close()
        return None