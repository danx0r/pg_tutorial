import sys, psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='%s'" % sys.argv[1])
except:
    print ("I am unable to connect to the database")
    exit()
print (conn)

cur = conn.cursor()
X = cur.execute

X("SELECT datname from pg_database")
rows = cur.fetchall()
print ("\nShow me the databases:\n")
for row in rows:
    print ("   ", row[0])

X("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
rows = cur.fetchall()
print ("\nShow me the tables:\n")
for row in rows:
    print ("   ", row[0])

X("drop table ttest")
X("create table ttest(foo text, bar int)")
X("insert into ttest values ('xoxy', 123)")
X("insert into ttest values ('Souza Bartholomew', 456)")
X("SELECT * from ttest")
rows = cur.fetchall()
print ("\nShow me the data:\n")
for row in rows:
    print ("   ", row)
