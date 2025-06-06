
from conexao import conecta_db
from cliente import opcao_menu
 


opcao_menu()

def menu_categoria():
    opcao_menu()

    while True: 
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()

        if opcao == "1":
            listar()
        elif opcao =="2":
            opcao_menu()
        elif opcao =="3":
          opcao_menu()
          
        elif opcao =="4":
          opcao_menu()
        elif opcao =="5":
            opcao_menu()              
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




