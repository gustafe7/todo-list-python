def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(tarefa + "\n")
    print("Tarefa salva com sucesso!")


def listar_tarefas():
    print("\n--- TAREFAS ---")
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")


def menu():
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
