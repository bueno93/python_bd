
from conexao import conecta_db
from menu import opcao_menu
 



def menu_usuario(titulo):
    opcao_menu(titulo)

    while True: 
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()

        if opcao == "1": 
            listar_usuario(conexao)
            

        elif opcao =="2":
            consultar_usuario_por_id(conexao)
            opcao_menu(titulo)

        elif opcao =="3":
            listar_usuario(conexao)
            inserir_usuario(conexao)
            listar_usuario(conexao)
            opcao_menu(titulo)

        elif opcao =="4":
            listar_usuario(conexao)
            alterar_usuario(conexao)
            listar_usuario(conexao)
            opcao_menu(titulo)

        elif opcao =="5":
            listar_usuario(conexao)
            deletar_usuario(conexao)
            listar_usuario(conexao)
            opcao_menu(titulo)
        
        elif opcao =="6":
            print ("Sair")  
            break  
        else :
            print ("Opção invalida, tente novamente. ")    


def login(conexao) -> bool:
    login = input("Digite o login: ")
    senha = input("Digite a Senha: ")
    cursor = conexao.cursor()
    sql_listar ="""select id, login, admin from usuario 
                    WHERE login = %s and senha = %s"""
    dados = (login,senha)
    cursor.execute(sql_listar,dados)
    registro = cursor.fetchone()
    if registro is None :
      print("Usuario e senha invalidos. ")
      return False
    else:
      admin = registro[2]
      return True

def listar_usuario(conexao):
    sql_listar =  """select id, login, admin from usuario
                    order by usuario.id asc
"""
    cursor = conexao.cursor() # cursor serve como o sql editor
    # execução de select no banco de dados
    cursor.execute(sql_listar) #recuparar todos os registros order by asc = ascendente e desc = descendente
    registros = cursor.fetchall() # fetchall retorna uma lista no caso dentro da variavel registro
    print("______________________________________________________")
    for registro in registros:
        print(f"|  ID: {registro[0]} - login: {registro[1]} - admin: {registro [2]}")
        print("______________________________________________________")

def consultar_usuario_por_id(conexao):
    id =  input("Digite o ID : ")
    cursor = conexao.cursor()
    cursor.execute("select id,login, admin from usuario where id =" + id)
    registro = cursor.fetchone()
    print(registro)
    if registro is None :
        print("Usuario não encontrado: ")
    else : 
        print(f"|ID : {registro[0]}")
        print(f"|login: {registro[1]}")
        print(f"|admin : {registro[2]}")
    

def inserir_usuario(conexao) :
    print("Inserindo o usuario..: ")
    cursor = conexao.cursor()
    login = input(" login : ")
    senha = (input("Senha : "))
    admin = (input("admin : "))
    sql_insert = "insert into usuario (login,senha,admin) values (%s,%s,%s)"
    dados = (login,senha,admin)
    cursor.execute(sql_insert,dados)
    conexao.commit()

def alterar_usuario(conexao):
    print("Alterando dados do usuario ...")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")

    login = input(" login : ")
    senha = (input("Senha : "))
    admin = (input("ADMIN: "))

    sql_update = "update usuario set login = %s, senha = %s, admin = %s,where id = %s "
    dados = (login,senha,admin,id)
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar_usuario(conexao):
    print("Deletando o usuario")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from usuario where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()


