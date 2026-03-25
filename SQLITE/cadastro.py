import sqlite3 as conector
conexao = conector.connect("estacio26.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (
                id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome varchar(50),
                curso varchar(50)
                )""")

# cursor.execute("""INSERT INTO alunos (nome, curso) VALUES ('Douglas', 'ADS')""")

# nome = input('Digite o nome do piralho: ')
# curso = input('Digite o curso do baixinho: ')

# cursor.execute("""INSERT INTO alunos(nome,curso)
#                VALUES (?,?)""", (nome, curso))

cursor.execute("""SELECT * FROM alunos""")
dados = cursor.fetchall()

for i in dados:
    print(i)

conexao.commit()