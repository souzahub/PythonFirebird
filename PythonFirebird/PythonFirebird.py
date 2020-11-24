
import firebirdsql

conn =firebirdsql.connect(user="SYSDBA",password="lmalma",database="c:\\bases\\ibestoqueti\\sgc_ti.gdb", host="170.81.40.199",charset="ANSI")

cur=conn.cursor()
cur.execute("select * from ESTOQUE")
for c in cur.fetchall():
    print(c)
conn.close
