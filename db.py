import sqlite3
import scrape

# NEED TO MAKE ALL DB TABLES REFER TO THE DB PATH

def get_gb():
    db_path = 'file:static/db/saved_properties.db'
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
    cursor.execute('DROP TABLE IF EXISTS saved_properties')
    cursor.execute('CREATE TABLE saved_properties(url TEXT, price TEXT, furnish_type TEXT, longitude REAL, latitude REAL)')
    connection.commit()

def add_property_to_db(scraped_data_dict, cursor, connection):
    if scraped_data_dict and type(scraped_data_dict) == dict:
        # if scrape.main() returns the dict, add to db
        cursor.execute('INSERT INTO saved_properties(url, price, furnish_type, longitude, latitude) VALUES(?, ?, ?, ?, ?)',(scraped_data_dict['url'], scraped_data_dict['price'], scraped_data_dict['furnish_type'], scraped_data_dict['longitude'], scraped_data_dict['latitude'])
        )
        connection.commit()
    else:
        # do nothing
        print('Nothing to add to db')

def query_db(cursor, connection):
    c, conn = connect_db()
    cursor.execute('SELECT * FROM saved_properties;')
    properties = c.fetchall()
    return properties
    
if __name__ == '__main__':
    db_path = get_gb()
    c, conn = connect_db()
    create_table(db_path, c, conn)
    scraped_data_dict = scrape.main()
    add_property_to_db(scraped_data_dict, c, conn)

    c.close()
    conn.close()
