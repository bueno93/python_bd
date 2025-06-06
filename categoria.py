
from conexao import conecta_db
from menu import opcao_menu
 


opcao_menu()

def menu_categoria(titulo):
    opcao_menu(titulo)

    while True: 
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()

        if opcao == "1":
            listar(conexao)
            opcao_menu(titulo)

        elif opcao =="2":
            consultar_categoria_por_id(conexao)
            opcao_menu(titulo)

        elif opcao =="3":
            listar(conexao)
            inserir_categoria(conexao)
            listar(conexao)
            opcao_menu(titulo)

        elif opcao =="4":
            listar(conexao)
            alterar_categoria(conexao)
            listar(conexao)
            opcao_menu(titulo)

        elif opcao =="5":
            listar(conexao)
            deletar_categoria(conexao)
            listar(conexao)
            opcao_menu(titulo)
        
        elif opcao =="6":
            print ("Sair")  
            break  
        else :
            print ("Opção invalida, tente novamente. ")    

def listar(conexao):
    cursor = conexao.cursor() # cursor serve como o sql editor
    # execução de select no banco de dados
    cursor.execute("select id,nome from categoria order by id desc") #recuparar todos os registros order by asc = ascendente e desc = descendente
    registros = cursor.fetchall() # fetchall retorna uma lista no caso dentro da variavel registro
    print("______________________________________________________")
    for registro in registros:
        print(f"|  ID: {registro[0]} - Nome {registro[1]}")
        print("______________________________________________________")

def consultar_categoria_por_id(conexao):
    id =  input("Digite o ID : ")
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria where id =" + id)
    registro = cursor.fetchone()
    print(registro)
    if registro is None :
        print("Categoria não encontrado: ")

def inserir_categoria(conexao) :
    print("Inserindo o Categoria..: ")
    cursor = conexao.cursor()
    nome = input(" Nome : ")
    sql_insert = "insert into categoria(nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()

def alterar_categoria(conexao):
    print("Alterarando a categoria...")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    nome = input("Nome: ")
    sql_update = "update categoria set nome = '" + nome + "' where id = " + id
    cursor.execute(sql_update)
    conexao.commit()

def deletar_categoria(conexao):
    print("Deletando a categoria")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from categoria where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()


