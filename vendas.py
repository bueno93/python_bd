from conexao import conecta_db
from datetime import datetime


def menu_vendas():
    print("|---------------------------|")
    print("|        Menu -> Vendas     |")
    print("|---------------------------|")
    print("| 1 - Consultar vendas      |")
    print("| 2 - Inserir Venda         |")
    print("| 3 - Sair                  |")
    print("|---------------------------|")

    conexao = conecta_db
    while True: 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
           consultar_vendas()
        elif opcao =="2":
           inserir_vendas()
           
        elif opcao =="3":
           break
        else:
           print("Opção Invalida!!!! Tente novamente: ")

def consultar_vendas():
   print("Nao implementado")

def inserir_vendas():
   id_cliente = input("Digite o ID do Cliente")
   data_venda = datetime.now()
   numero = 0
   valor_venda = 0        
