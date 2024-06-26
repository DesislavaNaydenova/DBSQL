import psycopg2


#connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object to the database
cursor = connection.cursor()

#Query1 - select all records from the artist table
#cursor.execute('SELECT * FROM "Artist"')

#Query2 - select only the name column from the artist table
#cursor.execute('SELECT "Name" FROM "Artist"')

#Query3 - select only Queen from the artist table
cursor.execute('SELECT * FROM "Artist"WHERE "Name" = %s',["Queen"])


# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
# results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)