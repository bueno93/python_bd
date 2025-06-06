from conexao import conecta_db

def opcao_menu():
    print ("|---------------------------------------------------------------------------------------| ")
    print ("|                             Cadastro                                                  | ")
    print ("|---------------------------------------------------------------------------------------| ")
    print ("| 1  - Listar | 2 - Consultar por ID | 3 - Inserir 4 - Alterar | 5 - Deletar | 6 - Sair | ")
    print ("|---------------------------------------------------------------------------------------| ")

def menu_cliente():
    opcao_menu()

    while True: 
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()

        if opcao == "1":
            listar(conexao) 
        elif opcao =="2":
            listar(conexao)
            consultar_cliente_por_id(conexao)  
            opcao_menu()     
        elif opcao =="3":
            inserir_clientes(conexao)
            listar(conexao) 
            opcao_menu()
        elif opcao =="4":
            print ("Alterar clientes ")
            listar(conexao)
            alterar_cliente(conexao)
            opcao_menu()
        elif opcao =="5":
            listar(conexao)
            deletar_cliente(conexao)
            opcao_menu()              
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

def alterar_cliente(conexao):
    print("Alterarando o Cliente")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    nome = input("Nome: ")
    sql_update = "update cliente set nome = '" + nome + "' where id = " + id
    cursor.execute(sql_update)
    conexao.commit()

def deletar_cliente(conexao):
    print("Deletando o Cliente")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from cliente where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()


    


