import requests as rq
import sqlite3 as sql3
import cryptography as crypto


nxurl = '''https://<instance>-engine-X.<region>.nexthink.cloud/2/
query?platform=windows&query=(select%20(hash%20sha1%20sha256)%20(from binary))&format=json'''

request = rq.get(nxurl)
binaries = request.json()

con=sql3.connect('MalBins.db')
cur=con.cursor()

for binary in binaries:
    md5=binary["hash"]
    sha1=binary["sha1"]
    sha256=binary["sha256"]
    cur.execute("SELECT * FROM hashes WHERE md5=? AND sha1=? AND sha256=?",
                (md5, sha1, sha256))
    match = cur.fetchone()
    if match:
        print(f'Match found for binary of md5 hash: {binary["hash"]}')
    else:
        print(f'No Matches Found.')

con.close()

        
#def is_malicious(hashes, malicious):
#    return hashes in malicious
    
# def do_nxql_query(url, port, username, password):
#     request=rq.get(url,)

# class NxqlQuery():
#     def __init__(self, url,port,username,password):
#         self.url= url
#         self.port=port
#         self.username=username
#         self.password=password
# nxurl = '''https://static-partner-01.demo.nexthink.cloud//2/
#             query?platform=windows&platform=mac_os&
#             query=(select%20(device_uid%20name)%20(from device))&format=json'''