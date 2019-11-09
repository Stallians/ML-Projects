import sqlite3

db_name = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
new_column = 'unique_names'
column_type = 'TEXT'
index_name = 'uniqNames'

# creating connection
conn = sqlite3.connect(db_name)
c = conn.cursor()

# adding a new column to table
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
    .format(tn=table_name, cn=new_column, ct=column_type))
# updating name in the existing record
c.execute("UPDATE {tn} SET {cn}='ashish' WHERE {idc}=(123456)"\
    .format(tn=table_name,cn=new_column, idc=id_column))

# creating a unique index
c.execute("CREATE INDEX {idxn} on {tn}({cn})"\
    .format(idxn=index_name, tn=table_name, cn=new_column))

# dropping the index
c.execute("DROP INDEX {idx}".format(idx=index_name))

# closing the connection
conn.commit()
conn.close()