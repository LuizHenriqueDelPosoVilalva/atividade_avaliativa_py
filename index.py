import datetime

def menu_remedio (lista, cont):
    print("--Gerenciamento de remedios--")
    while True:
        print("--Menu de opções--")
        print("1 - Cadastrar remedio -")
        print("2 - Listar remedios - ")
        print("3 - Buscar remedio pelo nome -")
        print("4 - Buscar remedios genericos -")
        print("5 - Buscar remedios não genericos -")
        print("6 - Atualizar campo atráves do nome - ")
        print("7 - Remover remedio")
        print("8 - calcular a media dos remedios em estoque")
        print("0 - Sair -")
        
        opcao = int(input(">> ")) 
        match opcao:
            case 1:
                print("--Cadastrar remedio--")
                cont = cadastrar(lista, cont)
            case 2:
                print("--Listar remedios cadastrados--")
                imprimir_remedios(lista)
            case 3:
                print("-- Buscar pelo remedio --")
                nome = input("Digite o nome do remedio: ")
                posicao = buscar_posicao(lista, nome)
                if posicao >= 0:
                    print("Remedio encontrado")
                    print(lista[posicao])
                else:
                    print("Remedio não encontrado")
            case 4:
                print("Lista de remedio genericos")
                buscar_generico(lista)
            case 5:
                print("Lista de remedios não genericos")
                buscar_nao_generico(lista)
            case 6:
                print("Atualizar campos do remedio")
                nome = input("Digite o nome do remedio que você deseje atualizar: ")
                posicao = buscar_posicao(lista, nome)
                if posicao >= 0:
                    atualizar_campo(posicao, lista)
                else:
                    print("Digite um remedio cadastrado")
            case 7:
                print("--Remover remedio--")
                nome = input("Digite o nome do remedio a ser excluido: ")
                posicao = buscar_posicao(lista, nome)
                if posicao >= 0:
                    remover_remedio(lista, posicao)
                else:
                   print("Digite um remedio cadastrado")
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
    hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
    remedio = dict(
        id = id, 
        nome = nome, 
        descricao = descricao, 
        generico = generico, 
        valor = valor, 
        quantidade = quantidade,
        hora = hora_atual
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
    print("Hora do cadastro: ", item['hora'])
    print("---------------------------------------")

def buscar_posicao (lista, nome):
    tamanho = len(lista)
    if tamanho > 0:
        for i in range(tamanho):
            if lista[i]['nome'] == nome:
                return i
            else:
                return -1
        else:
            return -1

def buscar_generico(lista):
    print("-Lista de remedios genericos-")
    if (not lista):
         return "A lista de alunos está vazia."

    for i in lista:
        nome_do_remedio = i['nome']
        generico = i['generico']
        if generico == True:
            apresentacao = f"{nome_do_remedio} é genérico"
        print(apresentacao)

def buscar_nao_generico(lista):
    print("-Lista de remedios não genericos-")
    if (not lista):
         return "A lista de alunos está vazia."

    for i in lista:
        nome_do_remedio = i['nome']
        generico = i['generico']
        if generico == False:
            print(f"{nome_do_remedio} não é generico")

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

cont = 0
lista = []
menu_remedio(lista, cont)