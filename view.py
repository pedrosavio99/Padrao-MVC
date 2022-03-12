from threading import local
import Controller

#primeiras coisa é verificar se os arquivos pra armazenar as infos existem
import os.path

from Models import Estoque
def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")

criarArquivos("categoria.txt", "estoque.txt" , "venda.txt")


if __name__ == "__main__": #so executa o arquivo dentro dele mesmo tem que ser o primeiro arquivo a rodar no sistema
    while True:
        local = int(input("\n============================LOBBY==========================\n\n"
                          "Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Vendas )\n"
                          "Digite 4 para acessar ( Produtos mais vendidos - relatório )\n"
                          "Digite 5 para acessar ( Sair do Lobby )\n"
                          "\n============================================================\n"))
        if local == 1:
            cat = Controller.ControllerCategoria()#esse cat é pra chamar as funções importadas do controller
            while True:
                decidir = int(input("\n============================================================\n\n"
                                    "Digite 1 para acessar ( Cadastrar uma categoria )\n"
                                    "Digite 2 para acessar ( Remover uma categoria )\n"
                                    "Digite 3 para acessar ( Alterar uma categoria )\n"
                                    "Digite 4 para acessar ( Mostrar Categorias )\n"
                                    "Digite 5 para acessar ( sair )\n"
                                    "\n============================================================\n"))
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja Remover\n")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que deseja Alterar\n")
                    novaCategoria = input("Digite a categoria para qual deseja Alterar\n")
                    cat.alterarCategoria(categoria,novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategorias()
                else:
                    break
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("\n============================================================\n\n"
                                    "Digite 1 para acessar ( Cadastrar produto )\n"
                                    "Digite 2 para acessar ( Remover um produto )\n"
                                    "Digite 3 para acessar ( Alterar um produto )\n"
                                    "Digite 4 para acessar ( ver o estoque )\n"
                                    "Digite 5 para acessar ( sair )\n"
                                    "\n============================================================\n"))
                if decidir == 1:
                    nome = input("Digite o nome do produto: \n")
                    preco = input("Digite o preco do produto: \n")
                    categoria = input("Digite a categoria do produto: \n")
                    quantidade = input("Digite a quantidade do produto: \n")

                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input("Digite o produto que deseja remover: \n")

                    cat.removerProduto(produto)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do produto que deseja alterar: \n")
                    nome = input("Digite o novo nome do produto: \n")
                    preco = input("Digite o novo preco do produto: \n")
                    categoria = input("Digite a nova categoria do produto: \n")
                    quantidade = input("Digite a nova quantidade do produto: \n")

                    cat.alterarProduto(nomeAlterar, nome, preco, categoria, quantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break
        
        elif local == 3:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para sair\n"))

                if decidir == 1:
                    nome = input('Digite o nome do produto: \n')
                    vendedor = input('Digite nome do vendedor: \n')
                    comprador = input('Digite o nome do cliente: \n')
                    quantidade = input('Digite a quantidade: \n')
                    cat.cadastrarVenda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    dataInicio = input("Digite a data de inicio no formato dia/mes/ano: \n")
                    dataTermino = input("Digite a data de termino no formato dia/mes/ano: \n")
                    cat.mostrarVenda(dataInicio, dataTermino)
                else:
                    break
        elif local == 4:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        else:
            break
            