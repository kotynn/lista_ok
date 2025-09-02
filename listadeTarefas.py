lista = []

def mostrar_lista():
    if lista:
        print("📋 Lista atual:")
        for i, item in enumerate(lista):
            print(i, "-", item)
    else:
        print("A lista está vazia!")

def adicionar():
    while True:
        item = input("Digite o item que você quer adicionar: ").strip()
        lista.append(item)
        print("Item adicionado com sucesso!")
        if input("Quer adicionar mais um item? [s/n]: ").lower() != "s":
            break

def atualizar():
    while True:
        if lista:
            try:
                mostrar_lista()
                posicao = int(input("Posição do item para atualizar: "))
                if 0 <= posicao < len(lista):
                    item_novo = input("Digite o item novo: ").strip()
                    lista[posicao] = item_novo
                    print("Item atualizado com sucesso!")
                else:
                    print("Posição inválida!")
            except ValueError:
                print("Digite um número válido!")
        else:
            print("A lista está vazia!")
            break
        if input("Quer atualizar mais um item? [s/n]: ").lower() != "s":
            break

def excluir():
    while True:
        if lista:
            try:
                mostrar_lista()
                posicao = int(input("Posição do item que quer excluir: "))
                if 0 <= posicao < len(lista):
                    removido = lista.pop(posicao)
                    print(f"Item '{removido}' removido com sucesso!")
                else:
                    print("Posição inválida!")
            except ValueError:
                print("Digite um número válido!")
        else:
            print("A lista está vazia!")
            break
        if input("Quer excluir mais um item? [s/n]: ").lower() != "s":
            break

def menu():
    while True:
        print('''
              [1] Adicionar
              [2] Atualizar
              [3] Excluir
              [4] Mostrar lista
              [5] Encerrar
              ''')
        
        try:
            escolha = int(input("Escolha uma das opções abaixo: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        match escolha:
            case 1: adicionar()
            case 2: atualizar()
            case 3: excluir()
            case 4: mostrar_lista()
            case 5:
                print("\nFLWWWWWW 👋")
                print("\n📋 Lista final:")
                mostrar_lista()
                break
            case _:
                print("Opção inválida, tente novamente!")

# executa o menu principal
menu()
