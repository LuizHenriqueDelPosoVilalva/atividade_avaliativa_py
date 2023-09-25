import datetime

def menu_remedio (lista, cont):
    lista_horarios = []
    print("--Gerenciamento de remedios--")
    while True:
        print("--Menu de opções--")
        print("1 - Cadastrar remedio -")
        print("2 - Listar remedios - ")
        print("3 - Buscar remedio pelo nome -")
        print("4 - Buscar remedios genericos -")
        print("5 - Buscar remedios não genericos -")
        print("6 - Atualizar campo atráves do nome - ")
        print("7 - Remover remedio -")
        print("8 - Calcular a media dos valores dos remedios -")
        print("9 - Calcular a media dos remedios em estoque -")
        print("10 - Buscar remedio com maior valor")
        print("11 - Buscar remedio de menor valor -")
        print("12 - Buscar palavra dentro da descrição -")
        print("13 - Listar horario de chamadas das funções")
        print("14 - Ordenar os remedios em ordem crescente ou decrescente -")
        print("0 - Sair -")
        
        opcao = int(input(">> ")) 
        match opcao:
            case 1:
                print("--Cadastrar remedio--")
                cont = cadastrar(lista, cont)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função cadastrar foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 2:
                print("--Listar remedios cadastrados--")
                imprimir_remedios(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de listar foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 3:
                print("-- Buscar pelo remedio --")
                nome = input("Digite o nome do remedio: ")
                posicao = buscar_posicao(lista, nome)
                print("Remedio encontrado")
                print(lista[posicao])
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de buscar remedio foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 4:
                print("Lista de remedio genericos")
                buscar_generico(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de listar remedios genericos foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 5:
                print("Lista de remedios não genericos")
                buscar_nao_generico(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de listar remedios NÃO genericos foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 6:
                print("Atualizar campos do remedio")
                nome = input("Digite o nome do remedio que você deseje atualizar: ")
                posicao = buscar_posicao(lista, nome)
                atualizar_campo(posicao, lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de atualizar campos do remedio foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 7:
                print("--Remover remedio--")
                nome = input("Digite o nome do remedio a ser excluido: ")
                posicao = buscar_posicao(lista, nome)
                remover_remedio(lista, posicao)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de remover remedio foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 8:
                print("--Media dos valores do projeto--")
                apresentar_media_valores(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de calcular media dos valores foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 9:
                print("--Media de remedios em estoque--")
                apresentar_media_quantidade(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de calcular media do estoque foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 10:
                print("--Maior valor--")
                maior_valor(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de consulta do maior valor foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 11:
                print("--Menor valor--")
                menor_valor(lista)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de consulta do menor valor foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 12:
                print("--Busca palavra--")
                nome = input("Digite o nome do remedio que queira fazer a pesquisa em sua descrição: ")
                palavra = input("Digite a palavra: ")
                pos = buscar_posicao(lista, nome)
                elemento = lista[pos]
                buscar_palavra(elemento, palavra)
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de buscar palavra foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)
            case 13:
                print(lista_horarios)
            case 14:
                print("ordenar pelo nome, faça sua escolha")
                print("-----------------")
                while True:
                    print("1 - Para crescente")
                    print("2 - Para decrescente")
                    print("0 - sair")
                    opcao = int(input(">> "))
                    match opcao:
                        case 1:
                            ordenar_crescente(lista)
                        case 2:
                            ordenar_descrescente(lista)
                        case 0:
                            break
                        case _:
                            print("Opção invalida")
                hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
                apresentação = f"A função de ordenar pelo nome do remedio foi chamada as: {hora_atual}"
                lista_horarios.append(apresentação)

            case 0:
                break
            case  _:
                print("Não existe essa opção")

def cadastrar(lista, cont):
    id = cont
    nome = input("Digite o nome do remedio: ")
    descricao = input("Digite a descrição do remedio: ")
    print("Generico ou não?")
    print("1 - sim")
    print("2 - não")
    opcao = int(input(">> "))
    while True:
        match opcao:
            case 1:
                generico = True
                break
            case 2:
                generico = False
                break
    valor = float(input("Digite o valor do remedio: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    remedio = dict(
        id = id, 
        nome = nome, 
        descricao = descricao, 
        generico = generico, 
        valor = valor, 
        quantidade = quantidade,
    )
    lista.append(remedio)
    cont+=1
    print("--Cadastro Efetuado com sucesso--")
    return cont
    
def imprimir_remedios(lista):
    for item in lista:
        modelo_de_apresentacao(item)

def modelo_de_apresentacao(item):
    print("id: ", item['id'])
    print("Nome: ", item['nome'])
    print("Descrição: ", item['descricao'])
    print("Genérico: ", item['generico'])
    print("Valor do remedio: ", item['valor'])
    print("Quantidade em estoque: ", item['quantidade'])
    print("---------------------------------------")

def buscar_posicao (lista, nome):
    tamanho = len(lista)
    if tamanho > 0:
        for i in range(tamanho):
            if lista[i]['nome'] == nome:
                return i

def buscar_generico(lista):
    if (not lista):
         return "A lista de alunos está vazia."

    tamanho = len(lista)
    for i in range(tamanho):
        nome_do_remedio = lista[i]['nome']
        generico = lista[i]['generico']
        if generico == True:
            apresentacao = f"{nome_do_remedio} é genérico"
            print(apresentacao)

def buscar_nao_generico(lista):
    if (not lista):
         return "A lista de alunos está vazia."

    tamanho = len(lista)
    for i in range(tamanho):
        nome_do_remedio = lista[i]['nome']
        generico = lista[i]['generico']
        if generico == False:
            apresentacao = f"{nome_do_remedio} não é generico"
            print(apresentacao)

def atualizar_campo(pos,lista):
    print("Menu de opções de atualização")
    while True:
        print("-1 atualizar nome do remedio -")
        print("-2 atualizar descrição do remedio -")
        print("-3 atualizar se é generico ou não -")
        print("-4 atualizar valor do remedio -")
        print("-5 atualizar quantidade do remedio -")
        print("-0 Sair da atualização -")
        
        opcao = int(input("Digite qual compo quer atualizar: "))
        match opcao:
            case 1:
                print("--Atualizar nome --")
                novo_nome = input("Digite o novo nome do remedio")
                lista[pos]['nome'] = novo_nome
            case 2:
                print("--Atualizar descrição--")
                nova_descricao = input("Digite a nova descrição do remedio")
                lista[pos]['descricao'] = nova_descricao
            case 3:
                print("Generico ou não?")
                print("-----------------")
                while True:
                    print("1- sim")
                    print("2 -não")
                    opcao_generico = int(input(">> "))
                    
                    match opcao_generico:
                        case 1:
                            lista[pos]['generico'] = True
                            break
                        case 2:
                            lista[pos]['generico'] = False
                            break
                        case _:
                            print("Opção invalida")
            case 4:
                print("--Atualizar valor--")
                valor_novo = float(input("Digite o novo valor: "))
                lista[pos]['valor'] = valor_novo
            case 5:
                print("--Atualizar quantidade--")
                quantidade_nova = float(input("Digite a nova quantidade: "))
                lista[pos]['quantidade'] = quantidade_nova
            case 0:
                print(lista[pos])
                break
            case _:
                print("Opção invalida")

def remover_remedio(lista, posicao):
    lista.pop(posicao)
    print("Remedio removido")

def media (soma, tamanho):
    media = soma/tamanho
    return media

def apresentar_media_valores (lista):
     lista_valores = []
     tamanho = len(lista)
     for i in range(tamanho):
         dado = lista[i]['valor']
         lista_valores.append(dado)
         soma = sum(lista_valores)
         media_valores = media(soma, tamanho)
         apresentar = f"A média dos valores dos remedios é de: {media_valores}"
     print(apresentar)

def apresentar_media_quantidade (lista):
     lista_quantidade = []
     tamanho = len(lista)
     for i in range(tamanho):
         dado = lista[i]['quantidade']
         lista_quantidade.append(dado)
         soma = sum(lista_quantidade)
         media_quantidade = media(soma, tamanho)
         apresentar = f"A média de quantidade de remedios em estoque é: {media_quantidade}"
     print(apresentar)

def maior_valor (lista):
    tamanho = len(lista)
    for i in range(0, tamanho):
        for j in range(0, 1):
            if lista[i]['valor'] < lista[j]['valor']:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    apresentação = f"o remedio de maior valor é o {lista[i]['nome']} com o valor de {lista[i]['valor']}"
    print(apresentação)

def menor_valor(lista):
    tamanho = len(lista)
    for i in range(0, tamanho):
        for j in range(0, 1):
            if lista[i]['valor'] > lista[j]['valor']:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
    apresentação = f"o remedio de menor valor é o {lista[i]['nome']} com o valor de {lista[i]['valor']}"
    print(apresentação)

def buscar_palavra(elemento, palavra):
    lista_descricao = elemento['descricao']
    palavras = lista_descricao.split()
    if palavra in palavras:
        resultado = f"A palavra {palavra} está contida na descrição '{lista_descricao}'"
    else:
        resultado = f"A palavra {palavra} NÃO está contida na descrição '{lista_descricao}'"
    print(resultado)

def ordenar_crescente(lista):
    lista_nova = lista.copy()
    tamanho = len(lista_nova)
    for i in range(0, tamanho):
        for j in range(0, i):
            if lista_nova[i]['nome'] < lista_nova[j]['nome']:
                temp = lista_nova[i]
                lista_nova[i] = lista_nova[j]
                lista_nova[j] = temp
    print(lista_nova)

def ordenar_descrescente(lista):
    lista_nova = lista.copy()
    tamanho = len(lista_nova)
    for i in range(0, tamanho):
        for j in range(0, i):
            if lista_nova[i]['nome'] > lista_nova[j]['nome']:
                temp = lista_nova[i]
                lista_nova[i] = lista_nova[j]
                lista_nova[j] = temp
    print(lista_nova)

cont = 0
lista = []
menu_remedio(lista, cont)