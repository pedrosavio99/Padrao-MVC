#caracteristicas do dados, os famosos modelos

#importar data pra por nas vendas
from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
        
class Produtos:
    def __init__(self,nome,preco,categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        
class Estoque:
    def __init__(self, produto: Produtos, quantidade): #perceba a forma de referenciar um classe dentro de outra
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendido: Produtos,vendedor,comprador, quantidadeVendida,data = datetime.now().strftime("%d/%m/%Y")): #perceba a forma de referenciar um classe dentro de outra
        self.itemvendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self,nome,cnpj,telefone,categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria
        
        
class Pessoa:
    def __init__(self, nome, telefone,cpf,email,endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa): #aqui eu n so referencio uma outra classe como faço com que os paremetros dela tbm sejam chamados sauqi
    def __init__(self,clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
        
