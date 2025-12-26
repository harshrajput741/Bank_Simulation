import sqlite3
def create_table():
    conobj = sqlite3.connect('mybank.sqlite')
    curobj = conobj.cursor()
    query = '''
create table accounts(
acn integer primary key autoincrement,
name text,
password text,
mobile text,
email text,
adhar text,
balance float,
opendate datetime)'''
    curobj.execute(query)
    conobj.commit()
    conobj.close()

if __name__ == '__main__':
    create_table()
