import sys, psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='%s'" % sys.argv[1])
except:
    print ("I am unable to connect to the database")
    exit()
print (conn)

cur = conn.cursor()
cur.execute("""SELECT datname from pg_database""")
rows = cur.fetchall()
print ("\nShow me the databases:\n")
for row in rows:
    print ("   ", row[0])
