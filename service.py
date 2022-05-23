import pyodbc

import time
time.sleep(10)
print("Started:")
#Add your own SQL Server IP address, PORT, UID, PWD and Database
conn_string = 'DRIVER={FreeTDS};SERVER=sqlserver;PORT=1433;DATABASE=Master;UID=SA;PWD=mssql1Ipw'
print(conn_string)
conn = pyodbc.connect(
    conn_string, autocommit=True)
cur = conn.cursor()
#This is just an example
cur.execute(
    f"SELECT [name] FROM sys.databases")
#conn.commit()
dbs = cur.fetchall()

print(dbs)
cur.close()
conn.close()