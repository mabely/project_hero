import scrape
import db

# for webapp integration
def return_db():
    c, conn = db.connect_db()
    properties = db.query_db(c, conn)
    print(properties)
    c.close()
    conn.close()

    return properties
# Seems to return empty list only


# for slack integration
return_db()