
import firebirdsql

usuario= (input("Ditite seu usuario: "))
senha = (input("Digite sua senha: "))
caminhoBanco = (input("Digite o caminho do seu Banco de Dados: "))
ip = (input("Digite o seu Host: "))


user = (usuario)
password = (senha)
caminhoBd = (caminhoBanco)
host = (ip)



conn =firebirdsql.connect(user=(user), password=(password), database=(caminhoBd), host=(host), charset="ANSI ")
 

cur=conn.cursor()
cur.execute("SELECT PRODUTO, ESTOQUE FROM ESTOQUE Where FORNEC = 'CASA DO COMPUTADOR' order by ID;")

for valor in cur.fetchall(): 
    print(valor)

conn.close
