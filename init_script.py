import sqlite3 as sql3

con=sql3.connect("MalBins.db")
cur=con.cursor()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS  "hashes" (
	"md5"	TEXT NOT NULL,
	"sha1"	TEXT NOT NULL,
	"sha256"	TEXT NOT NULL,
	"name"	TEXT
    );
    '''
)

md5_hashes=open('md5.txt','r').readlines()
sha1_hashes=open('sha1.txt','r').readlines()
sha256_hashes=open('sha256.txt','r').readlines()
bin_names=open('names.txt','r').readlines()
num = len(bin_names)

for i in range(num):
    name=bin_names[i]
    md5=md5_hashes[i]
    sha1=sha1_hashes[i]
    sha256=sha256_hashes[i]
    
    cur.execute('INSERT INTO hashes VALUES(?,?,?,?)',(md5,sha1,sha256,name))

con.commit()
con.close()