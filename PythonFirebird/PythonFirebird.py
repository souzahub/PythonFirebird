
import firebirdsql


usuario= (input("Digite seu usuario: "))
senha = (input("Digite sua senha: "))
caminhoBanco = (input("Digite o caminho do seu Banco de Dados: "))
ip = (input("Digite o seu Host: "))
nomeCampos = (input("select (nome dos campos):  "))
nomeTabela = (input("from(nome da tabela):  "))
where = (input("Where (campo desejado): "))
campoDesejado = (input(" igual a: "))


user = (usuario)
password = (senha)
caminhoBd = (caminhoBanco)
host = (ip)
nomeCampo = (nomeCampos)
nomeTabela = (nomeTabela)
where = (where)
campoDesejado = (campoDesejado)

conn =firebirdsql.connect(user=(user), password=(password), database=(caminhoBd), host=(host), charset="ANSI ")

cur=conn.cursor()
            
cur.execute("SELECT "+(nomeCampo)+" FROM "+(nomeTabela)+" Where "+(where)+ " = "+"'"+(campoDesejado)+"'"+" order by ID;")

for valor in cur.fetchall(): 
    print(valor)

conn.close
