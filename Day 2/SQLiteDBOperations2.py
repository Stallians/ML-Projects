# adding column

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
new_column1 = 'my_2nd_column'
new_column2 = 'my_3rd_column'
column_type = 'TEXT'
default_val = 'Hello world'

# Connecting to a database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    .format(tn=table_name, cn=new_column1, ct=column_type))

# add a new column with a default value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{dv}'"\
    .format(tn=table_name,cn=new_column2, ct=column_type, dv=default_val))

# commiting changes
conn.commit()
conn.close()
