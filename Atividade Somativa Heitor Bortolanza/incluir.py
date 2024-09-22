import json
import re
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

        for dicionarios in listaDados[chavePrincipal]:
            if codigo == dicionarios[chaveCodigo]:
                return True

        return False

def incluir(input_principal):

    with open("database.json", "r", encoding="utf-8") as arquivoBase:
        listaDados = json.load(arquivoBase)

    if input_principal == 1:

        codigo_estudante = validarInteiro("Digite o código do estudante a ser cadastrado: ")

        if existeCodigo("Estudantes", "codigo_estudante",codigo_estudante):
            print("Código já cadastrado!")
            return False

        novo_estudante = {
        "nome_estudante" : input("Digite o nome do estudante: "),
        "codigo_estudante" : codigo_estudante
        }

        listaDados["Estudantes"].append(novo_estudante)

    elif input_principal == 2:

        codigo_professor = validarInteiro("Digite o código do professor a ser cadastrado: ")

        if existeCodigo("Professores", "codigo_professor", codigo_professor):
            print("Código já cadastrado!")
            return False

        while True:
            cpf_professor = input("Difite o cpf do professor: ")
            if not re.match('^[0-9]{11}$', cpf_professor):
                print("CPF INVÁLIDO!")
                continue

            break

        novo_professor = {
        "codigo_professor" : codigo_professor,
        "nome_professor" : input("Digite o nome do professor: "),
        "cpf_professor" : cpf_professor
        }

        listaDados["Professores"].append(novo_professor)

    elif input_principal == 3:

        codigo_disciplina = validarInteiro("Digite o código da disciplina a ser cadastrada: ")

        if existeCodigo("Disciplinas", "codigo_disciplina", codigo_disciplina):
            print("Código já cadastrado!")
            return False

        nova_disciplina = {
        "codigo_disciplina" : codigo_disciplina,
        "nome_disciplina" : input("Digite o nome da disciplina: ")
        }

        listaDados["Disciplinas"].append(nova_disciplina)

    elif input_principal == 4:

        codigo_disciplina = validarInteiro("Digite o código da disciplina a ser cadastrada: ")
        if not existeCodigo("Disciplinas", "codigo_disciplina", codigo_disciplina):
            print("Código da disciplina não existe!")
            return False

        codigo_professor = validarInteiro("Digite o código do professor a ser cadastrado: ")
        if not existeCodigo("Professores", "codigo_professor", codigo_professor):
            print("Código do professor não existe!")
            return False

        codigo_turma = validarInteiro("Digite o código da turma a ser cadastrada: ")
        if existeCodigo("Turmas", "codigo_turma", codigo_turma):
            print("Código já cadastrado!")
            return False

        nova_turma = {
        "codigo_disciplina" : codigo_disciplina,
        "codigo_professor" : codigo_professor,
        "codigo_turma" : codigo_turma
        }

        listaDados["Turmas"].append(nova_turma)

    elif input_principal == 5:

        codigo_turma = validarInteiro("Digite o código da turma a ser cadastrada: ")
        if not existeCodigo("Turmas", "codigo_turma", codigo_turma):
            print("Código da turma não existe!")
            return False

        codigo_estudante = validarInteiro("Digite o código do estudante a ser cadastrado: ")
        if not existeCodigo("Estudantes", "codigo_estudante", codigo_estudante):
            print("Código do estudante não existe!")
            return False

        nova_matricula = {
        "codigo_turma" : codigo_turma,
        "codigo_estudante" : codigo_estudante
        }

        listaDados["Matriculas"].append(nova_matricula)

    with open("database.json", "w", encoding="utf-8") as arquivoBase:
        json.dump(listaDados, arquivoBase, ensure_ascii=False)

    return True