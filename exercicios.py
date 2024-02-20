import sqlite3
 
conexao = sqlite3.connect('Exercicios_banco_de_dados')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(30))')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(1, "Elias", 19, "Fisica")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(2, "Marinette", 23, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(3, "Rafael", 18, "Artes")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(5, "Manuel", 20, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(4, "Eduarda", 27, "Filosofia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(5, "Lucas", 30, "Engenharia")')

#cursor.execute('UPDATE alunos SET id=4 WHERE nome="Manuel"')
#cursor.execute('UPDATE alunos SET id=5 WHERE nome="Eduarda"')
#cursor.execute('UPDATE alunos SET id=6 WHERE nome="Lucas"')

# 3. Consultas Básicas
#dados = cursor.execute('SELECT * FROM alunos')
#dados = cursor.execute('SELECT nome, idade FROM alunos GROUP BY nome HAVING idade>20')
#dados = cursor.execute('SELECT nome, curso FROM alunos GROUP BY nome HAVING curso="Engenharia"')
#dados = cursor.execute('SELECT COUNT(id) FROM alunos')
#for alunos in dados:
#    print(alunos)

# 4. Atualização e Remoção
#cursor.execute('UPDATE alunos SET idade=20 WHERE nome="Elias"')
#cursor.execute('DELETE FROM alunos where id=3')

# 5. Criar uma Tabela e Inserir Dados
#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(1, "Michael", 25, 1.000)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(2, "Oscar", 32, 1.500)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(3, "Pamela", 40, 850)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(4, "James", 27, 3.260)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo)VALUES(5, "Angela", 48, 500)')

#cursor.execute('UPDATE clientes SET saldo=1000 WHERE saldo=1.000')
#cursor.execute('UPDATE clientes SET saldo=1550 WHERE saldo=1.500')
#cursor.execute('UPDATE clientes SET saldo=3260 WHERE saldo=3.260')

# 6. Consultas e Funções Agregadas
#dados2 = cursor.execute('SELECT nome, idade FROM clientes GROUP BY nome HAVING idade>30')
#dados2 = cursor.execute('SELECT AVG(saldo) FROM clientes')
#dados2 = cursor.execute('SELECT nome, MAX(saldo) FROM clientes')
#dados2 = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo>1000')

#for clientes in dados2:
#    print(clientes)  

# 7. Atualização e Remoção com Condições
#cursor.execute('UPDATE clientes SET saldo=1550 WHERE saldo=1.500')
#cursor.execute('DELETE FROM clientes where id=1')

# 8. Junção de Tabelas
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor DECIMAL(10,2), FOREIGN KEY(cliente_id) REFERENCES clientes(id))')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(1, 2, "Maquina de lavar roupa", 1952)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(2, 3, "Liquidificador", 99.90)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(3, 4, "Geladeira", 4.899)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(4, 5, "Ventilador", 147.80)')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(5, 0, "Mesa", 599.40)')

dados3 = cursor.execute('SELECT c.nomel, co.produto, co.valor FROM compras co JOIN clientes c ON co.cliente_id = c.id')

for compras in dados3:
    print(compras)

conexao.commit()  
conexao.close