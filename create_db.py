import sqlite3

def make_db():
    '''Makes database that usernames and messages will be saved to.
    '''
    conn = sqlite3.connect('database.bd')
    print('database created succesfully')
    conn.execute('CREATE TABLE users (username TEXT, message TEXT)')
    print('Table created succesfully')
    conn.close()

if __name__ == '__main__':
    make_db()


