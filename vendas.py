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

    conexao = conecta_db()
    while True: 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
           consultar_vendas()
        elif opcao =="2":
           inserir_vendas(conexao)
           
        elif opcao =="3":
           break
        else:
           print("Opção Invalida!!!! Tente novamente: ")

def consultar_vendas():
   print("Nao implementado")

def insert_item_venda(conexao, item_venda):
   cursor = conexao.cursor()
   sql_insert_item = """
        insert into itens_vendas(id_venda,id_produto,qtde,valor_unitario,valor_total)
        values (%s ,%s ,%s ,%s ,%s) """
   cursor.execute(sql_insert_item, item_venda)
   conexao.commit()  

def inserir_vendas(conexao):
   venda = alimentar_venda(conexao)
   itens_vendas = alimentar_itens_venda()
   id_venda = inserir_vendas(venda)

   for item in itens_venda:
      item_data = (id_venda, 
                   item['id_produto'], 
                   item['quantidade'], 
                   item['preco_unitario'],
                   item['valor_total'])
      insert_item_venda(conexao, item_data)

def alimentar_venda(conexao):
    id_cliente = input("Digite o ID do Cliente")
    data_venda = datetime.now()
    numero = input("Digite o número da venda: ")
    valor_venda = 0        
    return (id_cliente, data_venda, numero, valor_venda)

def insert_venda(conexao, id_cliente, data_venda, numero, valor_venda):
    cursor = conexao.cursor()
    sql_insert_venda ="""
       insert into venda(id_cliente,data_venda, numero_venda, valor_venda)
       values(%s,%s,%s,%s)
       RETURNING id
   """
    dados_venda = (id_cliente, data_venda ,numero, valor_venda)
    cursor.execute(sql_insert_venda,dados_venda)
    conexao.commit()
    venda_id = cursor.fetchone()[0]
    return venda_id

def alimentar_itens_venda():
    itens_venda = []
    while(True):
       id_produto = int(input("Digite o ID do produto: "))
       quantidade = float(input("Digite a quantidade : "))
       preco_unitario = float(input("Digite o preço unitário: "))
       valor_total = quantidade * preco_unitario

       itens_venda.append({"id_produto":id_produto,  #estrutura de array com itens
                          "quantidade":quantidade,
                          "preco_unitario":preco_unitario,
                          "valor_total":valor_total})
      
       print(itens_venda)
       continua = input(" Deseja adcionar outro item? (S/N)" )
      
       if continua == "N":
            break
       return itens_venda
def calcular_total_venda(itens_venda):
   total_venda = 0
   for item in itens_venda:
       total_venda = total_venda + ['valor_total']
   return total_venda
    

