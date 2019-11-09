# Inserting and updating data

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
column_name = 'my_2nd_column'

# Connecting to a database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# inserts an ID with a specific value in a second column
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print("ERRORL ID already exists in PRIMARY KEY column {}".format(id_column))

# tries to insert with a specific id (if it does not exists)
c.execute("INSERT OR IGNORE INTO {tn} ({idc}, {cn}) VALUES (123456, 'test')"\
    .format(tn=table_name, idc=id_column, cn=column_name))

# updates the newly inserted or pre-inserted query
c.execute("UPDATE {tn} SET {cn} = 'HI WORLD' WHERE {idf}=123456"\
    .format(tn=table_name, cn=column_name, idf=id_column))

# commiting changes
conn.commit()
conn.close()
