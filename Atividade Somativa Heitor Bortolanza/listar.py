import json
def listar(input_principal):

    with open("database.json", "r", encoding="utf-8") as arquivoBase:
        listaDados = json.load(arquivoBase)

    opcoes = list(listaDados)
    opcaoEscolhida = opcoes[input_principal - 1]
    i = 1

    if not listaDados[opcaoEscolhida]:
        print("Não há dados cadastrados!")

    for dicionario in listaDados[opcaoEscolhida]:
        for chave in dicionario.keys():
            print(chave + ": " + str(dicionario[chave]))
            if i%len(dicionario) == 0 and i != len(listaDados[opcaoEscolhida])*len(dicionario):
                print('')
            i += 1

    return True