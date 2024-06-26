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
#cursor.execute('SELECT * FROM "Artist"WHERE "Name" = %s',["Queen"])

#Query4 - select only by ArtistId #51 from the artist table
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')

#cursor.execute('SELECT * FROM "Artist"WHERE "ArtistId" = %s',[51])

#Query5 - select only the albums with  ArtistId #51 from the album table
#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 51')

#Query - select all tracks where the comppser is Queen from the track table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
#results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)