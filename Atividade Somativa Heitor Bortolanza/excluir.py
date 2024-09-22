import json
from listar import listar

def existeCodigo(chavePrincipal, chaveCodigo, codigo):

    with open("database.json", "r", encoding="utf-8") as arquivoBase:
        listaDados = json.load(arquivoBase)

        for dicionarios in listaDados[chavePrincipal]:
            if codigo == dicionarios[chaveCodigo]:
                return True

        return False
def excluir(input_principal):

    with open("database.json", "r", encoding="utf-8") as arquivoBase:
        listaDados = json.load(arquivoBase)

    opcoes = list(listaDados)
    opcaoEscolhida = opcoes[input_principal - 1]
    existe = False
    exclui = None

    if not listaDados[opcaoEscolhida]:
        print("Não há dados cadastrados!")
        return False

    listar(input_principal)

    user_input = int(input("\nDigite o código que deseja excluir: "))

    for dicionario in listaDados[opcaoEscolhida]:
        for valor in dicionario.values():
            if user_input == valor:
                existe = True
                exclui = dicionario
                break

    if existe:
        listaDados[opcaoEscolhida].remove(exclui)
        print("CÓDIGO REMOVIDO!")
    else:
        print("CÓDIGO NÃO ENCONTRADO!")

    with open("database.json", "w", encoding="utf-8") as arquivoBase:
        json.dump(listaDados, arquivoBase, ensure_ascii=False)

    return True