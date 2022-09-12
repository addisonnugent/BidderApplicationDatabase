"""

Date: 9/10/2022
Assignment: SQLite3 Database
About this project: Creating a database for a small scale application
Assumptions: N/A
All work below was performed by Addison Nugent

"""

import sqlite3

# connect to database
conn = sqlite3.connect('db_table.db')

# create cursor for database
cur = conn.cursor()

# drop table from database
conn.execute('''Drop table BIDDER''')
print("Bidder table dropped.")

# create table called BIDDER in database db_table
cur.execute('''CREATE TABLE Bidder(
BidderId INTEGER PRIMARY KEY NOT NULL,
BidderName TEXT NOT NULL,
PhoneNumber TEXT NOT NULL,
PrequalifiedUpperLimit INTEGER NOT NULL,
AppRoleLevel INTEGER NOT NULL,
LoginPassword TEXT NOT NULL);''')

print("Bidder Table created.")

# commit and save changes to database
conn.commit()

bidders = [(1, 'James Bond', '111-222-0007', 300000, 3, 'test123'),
           (2, 'Tina Whitefield', '333-444-5555', 2500000, 2, 'test456'),
           (3, 'Tim Jones', '777-888-9999', 125000, 1, 'test789'),
           (4, 'Jenny Smith', '3333-222-1111', 10000, 2, 'test321'),
           (5, 'Mike Hatfield', '555-444-3333', 2500, 1, 'test654'),
           (6, 'Steve Makers', '999-888-7777', 750, 3, 'test987')]

cur.executemany('Insert Into Bidder Values (?,?,?,?,?,?)', bidders)

# commit and save changes to database
conn.commit()
# Fetch all rows of query result which returns a list
cur.execute('SELECT * FROM Bidder;')
for row in cur:
    print(row)
# cl se database connection

"""
1) deletion SQL statement 1 row
2) update sql statement for 1 row
3) select data from a single table
4) select data from a table that limits the columns returned 
5) a select statment that selects data from a single table that limits the roes returned
6) select statemtn that selects from a single tabke that limits both the columns and rows returned
"""

# 1) deletion of 1 row
print("\nDelete Steve Makers")
conn.execute('''Delete from Bidder
                Where BidderId = 6;''')
cur.execute('''Select * from Bidder;''')
# commit and save changes to database
conn.commit()
# Fetch all rows of query result which returns a list
cur.execute('SELECT * FROM Bidder;')
for row in cur:
    print(row)


# 2) update of 1 row
print("\nUpdate PrequalifiedUpperLimit = 99999999 for Tim Jones")

conn.execute('''Update Bidder
                Set PrequalifiedUpperLimit = 99999999
                Where BidderId = 3;''')

cur.execute('''Select * from Bidder;''')
for row in cur:
    print(row)
conn.commit()
# 3) select data from a single table
print("\nA select statement that selects data from a single table")
cur.execute('SELECT * FROM Bidder;')
rows = cur.fetchall()
for row in rows:
    print(row)

# 4) select data from a single table limiting the columns returned
print("\nA select statement that selects data from a single table that limits the rows returned")
cur.execute('SELECT distinct BidderName, PrequalifiedUpperLimit FROM Bidder;')
rows = cur.fetchall()
for row in rows:
    print(row)

# 5) select data from a single table limiting the rows returned
print("\nA select statement that selects data from a single table that limits the columns returned")
cur.execute('SELECT * FROM Bidder WHERE BidderId < 3;')
rows = cur.fetchall()
for row in rows:
    print(row)

# 6) select data from a single table limiting the rows & columns returned
print("\nA select statement that selects data from a single table that limits the columns and rows returned")
cur.execute('SELECT distinct BidderName, PrequalifiedUpperLimit FROM Bidder WHERE BidderId < 4;')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
print('Connection closed.')
