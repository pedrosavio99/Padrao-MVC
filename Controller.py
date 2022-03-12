from genericpath import exists
from subprocess import list2cmdline
from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self,novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada')
        else:
            print('categoria ja existe nos registros')
            
#teste ds codigos
# a = ControllerCategoria()
# a.cadastrarCategoria('frios')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        
        if len(cat) <= 0:
            print('Categoria inexistente')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('categoria removida')
           
            with open('categoria.txt','w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
        #TODO: colocar sem categoria no estoque
        estoque = DaoEstoque.ler()
        #esse map serve pra formatar uma lista e subtituir valores nela
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome,x.produto.preco,"sem categoria"),x.quantidade)
                          if(x.produto.categoria == categoriaRemover) else(x), estoque ))
        with open('estoque.txt','w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|"
                            + i.produto.preco + "|"
                            + i.produto.categoria + "|"
                            + str(i.quantidade))
                arq.writelines('\n')
        
#TESTE DE REMOVER CATEGORIA
# a = ControllerCategoria()
# a.removerCategoria('Teste')
                    
#DEFINIÇÃO DE ALTERAR CATEGORIA PRECISA DE DOIS PARAMENTORS UM PRA SABER QUAL QUER MUDAR E OUTR PARA INFORMAR A ALTEREÇÃO DESEJADA
# a categoria que eu quero alterar precisa exister FILTRO 1
# FILTRO 2 a categoria que sera inserida não pode existir

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x)) #ver se a categoria informada realmente existe
        
        if len(cat) > 0: #aqui significa que encontrou a catgoria
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x)) #ver se a categoria que vc que alterar ja não existe
            if len(cat1) == 0:
                #aqui vou mudar a categoria selecionada com um map
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x),x))
                print('Categoria alterada')
                #TODO: ALTERAR A CATEGORIA TBM NO ESTOQUE
                estoque = DaoEstoque.ler()
                #esse map serve pra formatar uma lista e subtituir valores nela
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome,x.produto.preco, categoriaAlterada),x.quantidade)
                                if(x.produto.categoria == categoriaAlterar) else(x), estoque ))
                with open('estoque.txt','w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|"
                                    + i.produto.preco + "|"
                                    + i.produto.categoria + "|"
                                    + str(i.quantidade))
                        arq.writelines('\n')
        
                
            else:
                print('A categoria informada ja existe')
        else:
            print('Acategoria que procura ainda não existe')
            
        #depois deste trataemnto vc precisa reescrever seu BD
        with open('categoria.txt','w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

#testes de alterar categoria
# a = ControllerCategoria()
# a.alterarCategoria('teste1','teste5')

    def mostrarCategorias(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nenhuma categoria')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
#testes de Mostrar categoria
# a = ControllerCategoria()
# a.mostrarCategorias()

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco,categoria,quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y)) #filtro para saber se essa categoria existe
        est = list(filter(lambda x: x.produto.nome == nome, x)) #filtro pra saber se esse produo ja existe no estoque
        
        if len(h) >0:
            if len(est) == 0:
                produto = Produtos(nome,preco,categoria)
                DaoEstoque.salvar(produto,quantidade)
                print("Produto cadastrado!")
            else:
                print('produto já existe em estoque')
        else:
            print('categoria inexistene')
           
#teste de cadastrar produto
# a = ControllerEstoque().cadastrarProduto('banana','5','Frutas',10)           
            
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est)>0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:   
                    del x[i]
                    break  
            print('Produto removido')    
        else: 
            print('O produto não existe')
            
        with open('estoque.txt','w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|"
                               + i.produto.preco + "|"
                               + i.produto.categoria + "|"
                               + str(i.quantidade))
                arq.writelines('\n')

#teste de cadastrar produto
#a = ControllerEstoque().removerProduto('banana')  
    
    def alterarProduto(self, nomeAlterar,novoNome,novoPreco,novaCategoria,novaQuantidade):
       #aqui tem dois filtros um pra saber se a aategoria esixte e outro pra saber se o nome existe no estoque
       #na verdade tem 3 pois o item que quer alterar não pode existir no estoque
       x = DaoEstoque.ler()
       y = DaoCategoria.ler()
       h = list(filter(lambda x: x.categoria == novaCategoria, y)) #primeiro iltro
       if len(h) > 0:
           est = list(filter(lambda x: x.produto.nome == nomeAlterar, x)) #segundo filtro
           if len(est) > 0:
               est = list(filter(lambda x: x.produto.nome == novoNome, x)) #terceiro filtro
               if len(est) == 0:
                   #cndição grande mas vai entender que é so pra refazer uma nova lsita passando po cada paramentro do estoque
                   x = list(map(lambda x: Estoque(Produtos(novoNome,novoPreco,novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                   #so uma explicação que eu sei que vc vai bugar quando for reler, essa codição x:estoque... vai rearmazenar na lista os valores que a gente passou omo paramentro caso o nome do estoque seja igual ao nome que vc solicita alterar, caso contrario ele retorna o valor que ja tava no estoque
                   print("Produto alterado com sucesso")
               else:
                   print("produto ja cadastrado")
           else:
               print("Produto não encontrado")
               
           with open('estoque.txt','w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|"
                                + i.produto.preco + "|"
                                + i.produto.categoria + "|"
                                + str(i.quantidade))
                    arq.writelines('\n')
       else:
           print("Categoria inexistente")
        
#teste de alterar produto
#a = ControllerEstoque().cadastrarProduto('banana2','5','Frutas','20')  
# a = ControllerEstoque().alterarProduto('banana2', 'banana sem o 2','5','Frutas','50')  
    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("Estoque Vazio")
        else:
            print("==========Produtos==========")
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                    f"Preco: {i.produto.preco} brl\n"
                    f"Categoria: {i.produto.categoria}\n"
                    f"Quantidade: {i.quantidade}\n")
                print("--------------------")                
#teste de Mostrar estoque
#a = ControllerEstoque().mostrarEstoque()  

class ControllerVenda:
    def cadastrarVenda(self,nomeProduto, vendedor, comprador, quantidadeVendida):
        
        #RETURN 1: PRODUTO N EXISTE
        #RETURN 2: QUANTIDADE INSIPONIVEL
        #RETURN 3: VENDA EFETUADA
           
        x = DaoEstoque.ler()
        temp = [] #variavel temporaria pra armezenar os valores da venda antes de jogar proestoque, pq uuma vai pra venda e a outra vai atualizar o estoque sacou?
        existe = False #variavel pra ontrolar o for
        quantidade = False
        
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True #aqui acaba com a repetição desse for
                    if i.quantidade >= int(quantidadeVendida):
                        quantidade = True #aqui é pra ja filtrar se tem ou n a quantidade que o cliente quer
                        i.quantidade  = int(i.quantidade) - int(quantidadeVendida)
                        #aqui é a variavel pra quardar os dados da venda e depois enviar pro banco
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria),vendedor,comprador,quantidadeVendida)
                        #variave para mostrar o valor da compra
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido)
            #esse temp aqui vai salvar todos os arquivos idependente de ter vendido ou ou so pra atualizar o estoque
            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
        #cuidado onde termina esse for vc pode acabar se embanando pra cahar o erro kkkk
        arq = open('estoque.txt','w')
        arq.write("") #so pra limpar o arquivo
        
        for i in temp:
            with open('estoque.txt','a') as arq:
                arq.writelines(i.produto.nome + "|"
                                +i.produto.preco + "|"
                                +i.produto.categoria + "|"
                                + str(i.quantidade))
                arq.writelines('\n')
                
        if existe == False:
            print('O produto não existe') #na controller vc nem precisa por esses prints e sim apenas returns
            return 1
        elif not quantidade:
            print('Quantidade do produto indisponivel no estoque')
            return 2
        else:
            print(f'Venda Efetuada: {valorCompra} brl')
            return 3,valorCompra
            
#TESTE DE VENDA
#a = ControllerVenda().cadastrarVenda('banana', 'pedro', 'savio', 2)

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produts = [] #aqui eu armazeno um map para cada produto e a quantidade de vendas 
        for i in vendas:
            nome = i.itemvendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produts))
            if len(tamanho)>0:
                produts = list(map(lambda x: {'produto' : nome,'quantidade' : int(x['quantidade']) + int(quantidade)}
                                   if(x['produto']==nome) else(x),produts))
            else:
                produts.append({'produto':nome,'quantidade':int(quantidade)})
            
        #esse sorted vai ordenar do menor pro maior mas cmo queremos do maior pro menor add o reverse
        ordenado = sorted(produts, key=lambda k:k['quantidade'],reverse=True)
        
        print("Produtos mais vendidos: ")
        posicao_produto = 1
        for i in ordenado:
            print(f"Produto {posicao_produto}\n"
                    f"Nome: { i['produto']} - "
                    f"Quantidade: {i['quantidade']} \n\n")
            posicao_produto += 1
                          
#TESTE relatorio de produtos
#a = ControllerEstoque().cadastrarProduto('banana','5','Frutas',200000) 
#a = ControllerVenda().cadastrarVenda('banana2', 'pedro', 'savio', 45) 

    def mostrarVendas(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')
        
        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
                                         and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))
        
        cont = 1
        
        for i in vendasSelecionadas:
            print(f"======Venda [{cont}]=============")
            print(f"Nome: { i.itemvendido.nome } -- Data: {i.data}")
            cont += 1
            
#TESTE Mostrar vendas
#a = ControllerVenda().mostrarVendas('09/03/2022','11/03/2022') 


#controller fonecedor n feito pois é igual aos anteriores mudando apenas as variaveis e eu ja entendi o conceito