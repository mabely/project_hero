import sqlite3

def main_db():
    db_path = get_gb()
    c, conn = connect_db()
    create_table(db_path, c, conn)

def get_gb():
    db_path = 'file:saved_houses.db'
    # pass
    return db_path

def connect_db():
    db_path = get_gb()
    try:
        if get_gb():
            conn = sqlite3.connect(db_path, uri=True)
            c = conn.cursor()
            return c, conn
        else:
            raise EnvironmentError
    except Exception as e:
        print(e, 'Something went wrong with the db connection.')

def create_table(db_path, cursor, connection):
    # extract db name from db path
    cursor.execute('DROP TABLE IF EXISTS saved_houses')
    cursor.execute('CREATE TABLE saved_houses(url TEXT, price REAL, longitude REAL, latitude REAL)')
    connection.commit()

def add_property()
    pass
