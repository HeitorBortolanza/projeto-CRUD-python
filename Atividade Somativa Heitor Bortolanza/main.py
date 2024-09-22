import json
from incluir import incluir
from listar import listar
from atualizar import atualizar
from excluir import excluir

with open("database.json", "r", encoding="utf-8") as arquivoBase:
    listaDados = json.load(arquivoBase)

opcoes = list(listaDados)

def menu_principal():

    print("\n----- MENU PRINCIPAL -----")
    print("(1)   Gerenciar Estudantes.")
    print("(2)   Gerenciar Professores.")
    print("(3)   Gerenciar Disciplinas.")
    print("(4)   Gerenciar Turmas.")
    print("(5)   Gerenciar Matrículas.")
    print("(9)   Sair.\n")

    while True:
        try:
            user_input = int(input("Informe a opcao desejada: "))
        except ValueError:
            print("Por favor digite um dos numeros fornecidos")
        else:
            if user_input == 9:
                exit()
            elif 1 <= user_input <= 5:
                break
            else:
                print("Opcao invalida")

    while True:
        menu_operacoes(user_input)

def menu_operacoes(input_principal):

    print("\n***** [{}] MENU DE OPERACOES *****".format(opcoes[input_principal-1]))
    print("(1)  Incluir.")
    print("(2)  Listar.")
    print("(3)  Atualizar.")
    print("(4)  Excluir.")
    print("(9)  Voltar ao Menu Principal.\n")

    while True:
        try:
            user_input = int(input("Informe a opcao desejada: "))
        except ValueError:
            print("Por favor digite um dos numeros fornecidos")
        else:
            if user_input == 9:
                menu_principal()
            elif 1 <= user_input <= 4:
                break
            else:
                print("Opcao invalida")

    if user_input == 1:
        print("\n===== INCLUSAO =====\n")
        incluir(input_principal)
        return

    elif user_input == 2:
        print("\n===== LISTAGEM =====\n")
        listar(input_principal)
        return

    elif user_input == 3:
        print("\n===== ATUALIZAR =====\n")
        atualizar(input_principal)
        return

    elif user_input == 4:
        print("\n===== EXCLUSÃO =====\n")
        excluir(input_principal)
        return

def main():
    menu_principal()

if __name__ == "__main__":
    main()
