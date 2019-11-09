# querying rows - in a secure way to prevent SQL injection attacks
'''
    use ? instead of % formatter or .format() expression to build queries
'''

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


# Unsecure way
# Check if a certain ID exists and print its column contents
c.execute("SELECT * FROM {tn} WHERE {idc} = {my_id}"\
    .format(tn=table_name, idc=id_column, my_id=some_id))
id_exists = c.fetchone()

# Secure way
# Check if a certain ID exists and print its column contents
c.execute("SELECT * FROM {tn} WHERE {idc} = ?"\
    .format(tn=table_name, idc=id_column, my_id=some_id), (123456,))
id_exists = c.fetchone()

if id_exists:
    print("5:)", id_exists)
else:
    print("5:) id {} does not exists".format(some_id) )
