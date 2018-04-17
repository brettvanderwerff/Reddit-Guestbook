import sqlite3 as sql

def make_db():
    '''Makes database that usernames and messages will be saved to.
    '''
    conn = sql.connect('database.db')
    print('database created succesfully')
    conn.execute('CREATE TABLE users (username TEXT, message TEXT)')
    print('Table created succesfully')
    conn.close()

if __name__ == '__main__':
    make_db()


