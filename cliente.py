from conexao import conecta_db

def menu_cliente():


    print ("|--------------------------------------------------|")
    print ("|              Cadastro de cliente                 | ")
    print ("|--------------------------------------------------| ")
    print ("|              1  - Listar Clientes                | ")
    print ("|              2  - Consultar um CLiente(id)       | ")
    print ("|              3  - Inserir cliente                | ")
    print ("|              4  - Alterar                        | ")
    print ("|              5  - Deletar                        | ")
    print ("|              6  - Sair                           | ")
    print ("|--------------------------------------------------| ")

    while True: 
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()

        if opcao == "1":
            listar(conexao) 
        elif opcao =="2":
            listar(conexao)
            consultar_cliente_por_id(conexao)       
        elif opcao =="3":
            inserir_clientes(conexao)
            listar(conexao) 
        elif opcao =="4":
            print ("Alterar clientes ")
        elif opcao =="5":
            print ("Deletar clientes ")                
        elif opcao =="6":
            print ("Sair")  
            break  
        else :
            print ("Opção invalida, tente novamente. ")    

def listar(conexao):
    cursor = conexao.cursor() # cursor serve como o sql editor
    # execução de select no banco de dados
    cursor.execute("select id,nome from cliente order by id desc") #recuparar todos os registros order by asc = ascendente e desc = descendente
    registros = cursor.fetchall() # fetchall retorna uma lista no caso dentro da variavel registro
    print("______________________________________________________")
    for registro in registros:
        print(f"|  ID: {registro[0]} - Nome {registro[1]}")
        print("______________________________________________________")

def consultar_cliente_por_id(conexao):
    id =  input("Digite o ID : ")
    cursor = conexao.cursor()
    cursor.execute("select id,nome from cliente where id =" + id)
    registro = cursor.fetchone()
    if registro is None :
        print("Cliente não encontrado: ")
    else:
           print(f"|  ID: {registro[0]}")
           print(f"|  Nome {registro[1]}")
           print("______________________________________________________")

def inserir_clientes(conexao) :
    print("Inserindo o Cliente..: ")
    cursor = conexao.cursor()
    nome = input(" Nome : ")
    sql_insert = "insert into cliente(nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()
    


