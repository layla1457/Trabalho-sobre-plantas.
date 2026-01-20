from classificacoes import Briofita, Pteridofita, Gimnosperma, Angiosperma

Briofita.plantas.append(Briofita("Musgo", "Bryophyta"))
Pteridofita.plantas.append(Pteridofita("Samambaia", "Pteridophyta"))
Gimnosperma.plantas.append(Gimnosperma("Pinheiro", "Pinus"))
Angiosperma.plantas.append(Angiosperma("Macieira", "Malus domestica"))

def perguntar(pergunta):
    while True:
        resp = input(pergunta + " (s/n): ").lower()
        if resp in ("s", "n"):
            return resp == "s"
        print("Resposta inválida. Digite 's' ou 'n'.")

def identificar_planta():
    print("\nIdentificação da planta\n")

    vascular = perguntar("É vascular?")
    if not vascular:
        print("\nClassificação: Briófita")
        return

    semente = perguntar("Tem semente?")
    if not semente:
        print("\nClassificação: Pteridófita")
        return

    fruto = perguntar("Tem fruto?")
    if fruto:
        print("\nClassificação: Angiosperma")
    else:
        print("\nClassificação: Gimnosperma")

def mostrar_caracteristicas():
    print("\nEscolha a classificação:")
    print("1. Briófitas")
    print("2. Pteridófitas")
    print("3. Gimnospermas")
    print("4. Angiospermas")

    opcao = input("Opção: ")

    if opcao == "1":
        classe = Briofita
    elif opcao == "2":
        classe = Pteridofita
    elif opcao == "3":
        classe = Gimnosperma
    elif opcao == "4":
        classe = Angiosperma
    else:
        print("Opção inválida.")
        return

    if not classe.plantas:
        print("Nenhuma planta cadastrada.")
        return

    print("\nPlantas disponíveis:")
    for i, planta in enumerate(classe.plantas):
        print(f"{i + 1} - {planta.identificar()}")

    escolha = input("Escolha uma planta: ")

    try:
        planta = classe.plantas[int(escolha) - 1]
    except:
        print("Escolha inválida.")
        return

    print("\nCaracterísticas:")
    for c in planta.caracteristicas():
        print(f"- {c}")


##### menu principal ^_^ #####

def menu():
    while True:
        print("\n=== Sistema de Identificação de Plantas ===")
        print("1) Identificar uma planta")
        print("2) Ver características de plantas")
        print("0) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            identificar_planta()
        elif opcao == "2":
            mostrar_caracteristicas()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

menu()