# date and time operations

import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name = 'my_table_3'   # name of the table to be created
id_field = 'id' # name of the ID column
date_col = 'date' # name of the date column
time_col = 'time'# name of the time column
date_time_col = 'date_time' # name of the date & time column
field_type = 'TEXT'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute("CREATE TABLE {tn} ({c1} {ct} PRIMARY KEY)"\
     .format(tn=table_name, c1=id_field, ct=field_type))

# A) Adding a new column to save date insert a row with the current date
# in the following format: YYYY-MM-DD
# e.g., 2014-03-06
c.execute("ALTER TABLE {tn} ADD COLUMN {cn}".format(tn=table_name, cn=date_col))
 
# insert a new row with the current date and time, e.g., 2014-03-06
c.execute("INSERT INTO {tn} ({idc}, {dc}) VALUES('some_id', DATE('now'))"\
     .format(tn=table_name, idc=id_field, dc=date_col))

# B) Adding a new column to save date and time and update with the current time
# in the following format: HH:MM:SS
# e.g., 16:26:37
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
     .format(tn=table_name, cn=time_col))

# update row for the new current date and time column, e.g., 2014-03-06 16:26:37
c.execute("UPDATE {tn} SET {tc} = TIME('now') WHERE {idc}='some_id'"\
     .format(tn=table_name, tc=time_col, idc=id_field))


# C) Adding a new column to save date and time and update with current date-time
# in the following format: YYYY-MM-DD HH:MM:SS
# e.g., 2014-03-06 16:26:37
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
     .format(tn=table_name, cn=date_time_col))

# update row for the new current date and time column, e.g., 2014-03-06 16:26:37
c.execute("UPDATE {tn} SET {dtc} = DATETIME('now') WHERE {idc}='some_id'"\
     .format(tn=table_name, dtc=date_time_col, idc=id_field))

# The database should now look like this:
# id         date           time        date_time
# "some_id1" "2014-03-06"   "16:42:30"  "2014-03-06 16:42:30"

# 4) Retrieve all IDs of entries between 2 date_times
c.execute("SELECT {idc} FROM {tn} WHERE {dtc} BETWEEN '2018-11-09 07:21:44' AND '2020-11-09 07:21:44'"\
    .format(idc=id_field, tn=table_name, dtc=date_time_col))
all_records = c.fetchall()
print("All entries between 2018 and 2020: ", all_records)

# 5) Retrieve all IDs of entries between that are older than 1 day and 12 hrs
c.execute("SELECT {idc} FROM {tn} WHERE DATE('now') - {dtc} >= 1 AND TIME('now') - {tc} >=12"\
    .format(idc=id_field, tn=table_name, dtc=date_time_col, tc=time_col))
all_records = c.fetchall()
print("All records older than 1yr and 12 hrs : ", all_records)

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()