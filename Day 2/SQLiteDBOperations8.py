# table metadata

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_3'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# getting column data
c.execute("PRAGMA TABLE_INFO({})".format(table_name))

# it will return a list of tuples in format [(id, name, field_type, notnull, def val, pk)]
names = [col[1] for col in c.fetchall()]
print("names = ", names)

# closing connection
conn.close()