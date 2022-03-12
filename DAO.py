from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls,categoria):
        with open('categoria.txt','a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls): #essa função é onde a gente le o bd txt e armazena os dados do txt em nosso modelo de categorias
        with open('categoria.txt','r') as arq:
            cls.categoria = arq.readlines()
        #SO PARA PODER RETIRAR O \N DE NOSSAS CATEGORIAS
        cls.categoria = list(map(lambda x: x.replace('\n',''), cls.categoria))
        #print(cls.categoria)
        
        cat = []
        
        for i in cls.categoria: #jogar dentro de nosso modelo
            cat.append(Categoria(i))
        
        return cat
#TESTES DE NOSSAS CLASSES       
#DaoCategoria.salvar("Frutas")
#DaoCategoria.ler()

class DaoVenda:
    @classmethod
    def salvar(cls,venda: Venda):
        with open('venda.txt','a') as arq:
            #mano isso é muito legal ele pega o paremtro nome que ta dentro do produto em venda que loucuraaaa
            arq.writelines(venda.itemvendido.nome + "|"
                           + venda.itemvendido.preco + "|"
                           + venda.itemvendido.categoria + "|"
                           + venda.vendedor + "|"
                           + venda.comprador + "|"
                           + str(venda.quantidadeVendida) + "|"
                           + venda.data)
            
            arq.writelines('\n')
            
    @classmethod        
    def ler(cls):
        with open('venda.txt','r') as arq:
            cls.venda = arq.readlines()
            
        #SO PARA PODER RETIRAR O \N DE NOSSAS CATEGORIAS
        cls.venda = list(map(lambda x: x.replace('\n',''), cls.venda))
        #SO PARA PODER criar uma lista separada pelos pipes
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        #print(cls.venda)
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0],i[1],i[2]),i[3],i[4],i[5])) #esse is são o nome preço e categoria do produto
        return vend
    
#TESTES DE NOSSAS CLASSES
# produtofic = Produtos('banana','5','misseis')
# vendafic = Venda(produtofic,"pedro",'marcos','3') # CRIAR UM PRODUTO FICTICIO
# DaoVenda.salvar(vendafic) # ADD UM PRODUTO FICTICIO
# x =  DaoVenda.ler()
# print(x[0].itemvendido.nome)

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos,quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|"
                           + produto.preco + "|"
                           + produto.categoria + "|"
                           + str(quantidade))
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open('estoque.txt','r') as arq:
            cls.estoque = arq.readlines()
        #SO PARA PODER RETIRAR O \N DE NOSSAS CATEGORIAS
        cls.estoque = list(map(lambda x: x.replace('\n',''), cls.estoque))
        #SO PARA PODER criar uma lista separada pelos pipes
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))  
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0],i[1],i[2]),int(i[3])))
                
        return est
    

#================================ATENCAO!!!============================================


#esseas 3 casses eu cRieI mas não utilizarei elas pois o conceito ja foi entendido      
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor : Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|"
                            + fornecedor.cnpj + "|"
                            + fornecedor.telefone + "|"
                            + fornecedor.categoria)
            arq.writelines('\n')    
            
    @classmethod
    def ler(cls):
        with open('fornecedores.txt','r') as arq:
            cls.fornecedores = arq.readlines()
            
        #SO PARA PODER RETIRAR O \N DE NOSSAS CATEGORIAS
        cls.fornecedores = list(map(lambda x: x.replace('\n',''), cls.fornecedores))
        #SO PARA PODER criar uma lista separada pelos pipes
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))  
        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0],i[1],i[2],i[3]))
                
        return forn   
    
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + "|"
                            + pessoas.telefone + "|"
                            + pessoas.cpf + "|"
                            + pessoas.email + "|"
                            + pessoas.endereco)
            arq.writelines('\n')    
            
    @classmethod
    def ler(cls):
        with open('clientes.txt','r') as arq:
            cls.clientes = arq.readlines()
            
        #SO PARA PODER RETIRAR O \N DE NOSSAS CATEGORIAS
        cls.clientes = list(map(lambda x: x.replace('\n',''), cls.clientes))
        #SO PARA PODER criar uma lista separada pelos pipes
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))  
        clie = []
        for i in cls.clientes:
            clie.append(Pessoa(i[0],i[1],i[2],i[3],i[4]))
                
        return clie   
    
class DaoFuncionario:
    @classmethod
    def salvar(cls, funionario : Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funionario.clt + "|"
                            + funionario.nome + "|"
                            + funionario.telefone + "|"
                            + funionario.cpf + "|"
                        + funionario.email + "|"
                        + funionario.endereco)
            arq.writelines('\n')    
            
    @classmethod
    def ler(cls):
        with open('funcionarios.txt','r') as arq:
            cls.funcionarios = arq.readlines()
            
        #SO PARA PODER RETIRAR O \N DE NOSSAS CATEGORIAS
        cls.funcionarios = list(map(lambda x: x.replace('\n',''), cls.funcionarios))
        #SO PARA PODER criar uma lista separada pelos pipes
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))  
        func = []
        for i in cls.funcionarios:
            func.append(Funcionario(i[0],i[1],i[2],i[3],i[4],i[5]))
                
        return func   
    
