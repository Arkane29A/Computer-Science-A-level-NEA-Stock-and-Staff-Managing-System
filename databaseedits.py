import sqlite3 

conn = sqlite3.connect("SoftwareData.db")
scursor = conn.cursor()
# scursor.execute("""SELECT * FROM UserInfo""")

# print(scursor.fetchall())

# scursor.execute("""DELETE FROM UserInfo""")
# conn.commit()

# addColumn = "ALTER TABLE UserINFO ADD COLUMN Identifier"

# scursor.execute(addColumn)
# conn.commit()


# scursor.execute("""SELECT Identifier FROM UserInfo""")
# x = scursor.fetchone()
# print (len(x))



# scursor.execute("""CREATE TABLE UserInfo (Username text, Password text, SCODE, Identifier)""")
# conn.commit()


# scursor.execute("""CREATE TABLE StaffInfo (DAY text, T1 text, T2 text, T3 text, T4 text, T5 text)""")

# scursor.execute("""DROP TABLE StaffInfo""")


# scursor.execute("""CREATE TABLE UserInfo (Username text, Password text, SCODE, Identifier)""")
# conn.commit()

# scursor.execute("""DROP TABLE UserInfo""")

# temp = "ID1"
# scursor.execute('INSERT INTO UserInfo (Identifier) VALUES (?)', [temp])
# conn.commit()

# scursor.execute("INSERT INTO UserInfo VALUES ('Saadhzahid', 'saadh123', 8958, 'ID1')")
# conn.commit()


# conn.commit()

# scursor.execute("""SELECT * FROM UserInfo""")
# print(scursor.fetchone())


# scursor.execute("""SELECT * FROM StockInfo""")
# print(scursor.fetchall())



# scursor.execute("INSERT INTO StockInfo VALUES ('A321', 'Furniture', 'TableMakers', 'table', 6, 12.00, 9)")
# scursor.execute("INSERT INTO StockInfo VALUES ('A111', 'Toy', 'ToyShop', 'Lego', 8, 9.00, 3)")

# scursor.execute("INSERT INTO StaffInfo VALUES ('Monday', 'Michael', 'Michael', 'Bill', 'Bill', 'Ross')")
# scursor.execute("INSERT INTO StaffInfo VALUES ('Tuesday', 'Pounds', 'Dog', 'Shoobob', 'Dog', 'Jenny')")


conn.commit()
        
# x = 'Forks'

# scursor.execute('UPDATE StockInfo SET Item=? WHERE ItemID = "A440" ', [x])
# conn.commit()

conn.close()

