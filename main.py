#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
pedro = Pessoa(1, "Pedro Lara")
print(pedro)

#Quero mostrar só o nome
print(pedro.nome)