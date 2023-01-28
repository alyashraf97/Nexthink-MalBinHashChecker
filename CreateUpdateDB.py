import sqlite3 as sql3
import csv

# Connect to the DB (or create it if it doesn't exist)
con=sql3.connect("MalBins.db")
cur=con.cursor()

# Create DB if it doesn't exist
cur.execute(
    '''CREATE TABLE IF NOT EXISTS "hashes" (
        "md5" TEXT NOT NULL UNIQUE,
        "sha1" TEXT NOT NULL UNIQUE,
        "sha256" TEXT NOT NULL UNIQUE
    );
    '''
)
con.commit()

# Opens hashes CSV file into new_hashes list of tuples
with open('hashes.csv', newline='') as f:
    reader=list(csv.reader(f))
    new_hashes = [tuple(row) for row in reader]
    
# Placeholder query function
def insert_hashes(hashes):
    placeholders= ', '.join('?'*len(hashes[0]))
    sql = f'INSERT OR IGNORE INTO hashes VALUES ({placeholders})'
    con.executemany(sql, hashes)
    con.commit()
 

# Creates DB Entries
insert_hashes(new_hashes)
con.close()


# db = con.execute('SELECT * from hashes')
# print(db.fetchall())
#print(new_hashes)