
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
    despesa = cadastrar_despesa()
    despesas.append(despesa)

    opcao = input("\nDeseja cadastrar outra despesa? (s/n): ")

    if opcao.lower() == "n":
        break

listar_despesas(despesas)
mostrar_resumo(despesas)
