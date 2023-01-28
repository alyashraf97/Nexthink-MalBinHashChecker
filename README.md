# Nexthink-MalBinHashChecker
Malicious Binary Hash Checker using Nexthink API, NXQL, Python and SQLite

# How to use
Add your hash entries into the CSV file with a comma delimitter and no text qualifier in the following order of columns: md5, sha1, sha256.  
  
  Example:  
  md5_1, sha1_1, sha256_1  
  md5_2, sha1_2, sha256_2  
  md5_3, sha1_3, sha256_3  
  md5_4, sha1_4, sha256_4  
  
Run the CreateUpdateDB.py script in order to create your DB if it doesn't exist, or updated with new entries in your hashes.csv  
  
Run the CheckMaliciousBins.py in order to query the Nexthink database (authentication isn't implemented yet) and check if there are any malicious binaries in your environment.
