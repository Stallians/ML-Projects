# querying rows

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
some_id = 12345
column2 = 'my_2nd_column'
column3 = 'my_3rd_column'

# creating the connection
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# selecting all rows from database 
c.execute("SELECT * FROM {tn} WHERE {cn} = '{cv}'"\
    .format(tn=table_name, cn=column2, cv='HI WORLD'))
all_results = c.fetchall()
print('1:) ', all_results)

# selecting a particular column for rows that match a value in column_1
c.execute("SELECT {rcn} FROM {tn} WHERE {cn} = '{cv}'"\
    .format(tn=table_name, cn=column2, cv='HI WORLD', rcn=column3))
all_results = c.fetchall()
print('2:) ', all_results)

# selecting two particular columns for rows that match a value in column_1
c.execute("SELECT {c1}, {c2} FROM {tn} WHERE {cn} = '{cv}'"\
    .format(tn=table_name, cn=column2, cv="HI WORLD", c1=column3, c2=column2))
all_results = c.fetchall()
print('3:) ', all_results)

# Selecting only up to 10 rows that match a certain value in 1 column
c.execute("SELECT * FROM {tn} WHERE {idc} = 'Hello world' LIMIT 10"\
    .format(tn=table_name, idc=column3))
all_results = c.fetchall()
print("4:)",all_results)

# Check if a certain ID exists and print its column contents
c.execute("SELECT * FROM {tn} WHERE {idc} = {my_id}"\
    .format(tn=table_name, idc=id_column, my_id=some_id))
id_exists = c.fetchone()
if id_exists:
    print("5:)", id_exists)
else:
    print("5:) id {} does not exists".format(some_id) )
