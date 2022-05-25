import pyodbc

import time
time.sleep(10)
print("Started:")
#Add your own SQL Server IP address, PORT, UID, PWD and Database
conn_string = 'DRIVER={FreeTDS};SERVER=sqlserver;PORT=1433;DATABASE=tempdb;UID=SA;PWD=mssql1Ipw'
print(conn_string)
conn = pyodbc.connect(
    conn_string, autocommit=True)
cur = conn.cursor()
#This is just an example
cur.execute(
    f"CREATE TABLE products (product_name nvarchar(50),price int)")

print('done table')
insert = "INSERT INTO products (product_name, price) VALUES "
i = 0
while i < 1000:
    i += 1
    chu = f"('Item {i}',{i})"
    insert = insert + chu
    if i < 1000:
        insert = insert + ", "
conn.execute(insert)      
#conn.commit()
#dbs = cur.fetchall()

print('done')
cur.close()
conn.close()