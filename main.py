#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
pedro = Pessoa(1, "Pedro Lara")
print(pedro)

#Quero mostrar só o nome
print(pedro.nome)

print()

print("DAQUI PRA FRENTE É ACESSO AO BANCO...")
print()

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)