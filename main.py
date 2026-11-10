
def cadastrar_despesa():
    print("\n========== NOVA DESPESA ==========")

    despesa = {
        "descricao": input("Descrição da despesa: "),
        "categoria": input("Categoria da despesa: "),
        "valor": float(input("Valor da despesa: ")),
        "data": input("Data da despesa (dd/mm/aaaa): ")
    }

    return despesa


def listar_despesas(despesas):
    print("\n========== DESPESAS REGISTRADAS ==========")

    for despesa in despesas:
        print(f"\nDescrição: {despesa['descricao']}")
        print(f"Categoria: {despesa['categoria']}")
        print(f"Valor: R$ {despesa['valor']:.2f}")
        print(f"Data: {despesa['data']}")


def calcular_total(despesas):
    total = 0

    for despesa in despesas:
        total += despesa["valor"]

    return total


def mostrar_resumo(despesas):
    total = calcular_total(despesas)

    print("\n========== RESUMO ==========")
    print(f"Quantidade de despesas: {len(despesas)}")
    print(f"Total de gastos: R$ {total:.2f}")


# PROGRAMA PRINCIPAL

print("================================")
print("       EXPENSE TRACKER")
print("Bem-vindo ao seu controle de gastos!")
print("================================")

despesas = []

while True:
    print("\n=== MENU ===")
    print("1. Cadastrar nova despesa")
    print("2. Listar despesas e resumo")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        despesa = cadastrar_despesa()
        despesas.append(despesa)
    elif opcao == "2":
        listar_despesas(despesas)
        mostrar_resumo(despesas)
    elif opcao == "3":
        print("Saindo do programa...")
        break  # Aqui ele para o loop e encerra de vez!
    else:
        print("Opção inválida! Tente novamente.")