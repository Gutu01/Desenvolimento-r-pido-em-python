import sqlite3 as conector
conexao = conector.connect('estacio26.db')
cursor = conexao.cursor()

while True:
    print('\n------------Menu------------')
    print('1 - Cadastrar Aluno')
    print('2 - Listar alunos')
    print('3 - Sair')

    opcao = int(input('Digite sua escolha: '))

    match opcao:
        case 1:
            nome = input('\nDigite o nome do aluno: ')
            curso = input('\nDigite o curso do aluno: ')

            cursor.execute('INSERT INTO alunos(nome, curso) VALUES (?, ?)', (nome, curso))
            conexao.commit()

        case 2:
            cursor.execute('SELECT * FROM alunos')
            dados = cursor.fetchall()
            for i in dados:
                print(i)

        case 3:
            break