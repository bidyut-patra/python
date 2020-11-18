
import sqlite3

def main():
    print('connect database')
    db = sqlite3.connect('db-api.db')
    cursor = db.cursor()
    print('create table')
    cursor.execute("DROP TABLE IF EXISTS Employee")
    cursor.execute("""
        CREATE TABLE Employee (
            Name string NOT NULL,
            Dept string NOT NULL
            )
        """)
    print('insert row')
    cursor.execute("""
        INSERT INTO Employee
        VALUES('Bidyut', 'Industry')
        """)
    print('insert row')
    cursor.execute("""
        INSERT INTO Employee
        VALUES('Amit', 'Industry')
        """)        
    print('insert row')
    cursor.execute("""
        INSERT INTO Employee
        VALUES('Zakir', 'Digital')
        """)        
    print('commit database')
    db.commit()
    print('row count')
    cursor.execute("""
        SELECT COUNT(*) FROM Employee
        """)
    count = cursor.fetchone()[0]
    print(f'There are {count} rows in the table')
    print('read the table')
    for row in cursor.execute('SELECT rowid, Name, Dept FROM Employee'):
        print(row)
    print('drop the table')
    cursor.execute("""
        DROP TABLE Employee
        """)
    print('close the database')
    db.close()

if __name__ == "__main__":
    main()