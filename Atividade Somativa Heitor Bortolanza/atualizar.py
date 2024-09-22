import json
from listar import listar
from incluir import incluir

def validarInteiro(menasagem):
    while True:
        try:
            inputTeste = int(input(menasagem))
        except ValueError:
            print("Por favor, digite apenas números")
        else:
            break

    return inputTeste

def existeCodigo(chavePrincipal, chaveCodigo, codigo):
    with open("database.json", "r", encoding="utf-8") as arquivoBase:
        listaDados = json.load(arquivoBase)

    teste = False
    while not teste:

        for dicionarios in listaDados[chavePrincipal]:
            if codigo == dicionarios[chaveCodigo]:
                teste = True
                break

        return teste

def atualizar(input_principal):

    with open("database.json", "r", encoding="utf-8") as arquivoBase:
        listaDados = json.load(arquivoBase)

    opcoes = list(listaDados)
    opcaoEscolhida = opcoes[input_principal - 1]
    codigo_velho = None

    if not listaDados[opcaoEscolhida]:
        print("Não há dados cadastrados!")
        return False

    listar(input_principal)

    if input_principal == 1:

        codigo_velho = validarInteiro("\nDigite o código do estudante a ser atualizado: ")

        if not existeCodigo("Estudantes", "codigo_estudante",codigo_velho):
            print("Código do estudante não existe!")
            return False

    elif input_principal == 2:

        codigo_velho = validarInteiro("Digite o código do professor a ser atualizado: ")

        if not existeCodigo("Professores", "codigo_professor",codigo_velho):
            print("Código do professor não existe!")
            return False

    elif input_principal == 3:

        codigo_velho = validarInteiro("Digite o código da disciplina a ser atualizada: ")

        if not existeCodigo("Disciplinas", "codigo_disciplina", codigo_velho):
            print("Código da disciplina não existe!")
            return False

    elif input_principal == 4:

        codigo_velho = validarInteiro("Digite o código da turma a ser atualizada: ")
        if not existeCodigo("Turmas", "codigo_turma", codigo_velho):
            print("Código da turma não existe!")
            return False

    elif input_principal == 5:

        codigo_velho = validarInteiro("Digite o código do estudante a ser atualizado: ")
        if not existeCodigo("Estudantes", "codigo_estudante", codigo_velho):
            print("Estudante não está matriculado!")
            return False

    if incluir(input_principal):
        for dicionario in listaDados[opcaoEscolhida]:
            for valor in dicionario.values():
                if codigo_velho != valor:
                    continue
                listaDados[opcaoEscolhida].remove(dicionario)

    with open("database.json", "w", encoding="utf-8") as arquivoBase:
        json.dump(listaDados, arquivoBase, ensure_ascii=False)

    return True