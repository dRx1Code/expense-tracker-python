
def cadastrar_despesa():
    print("\n========== NOVA DESPESA ==========")

    descricao = input("Descrição da despesa: ")
    categoria = input("Categoria da despesa: ")

    # Validação do valor com try/except
    while True:
        try:
            # Substitui vírgula por ponto caso o usuário digite 15,50
            valor_str = input("Valor da despesa: ").replace(',', '.')
            valor = float(valor_str)
            break
        except ValueError:
            print("❌ Valor inválido! Digite apenas números (use ponto para decimais).")

    # Entrada da data facilitada
    data_input = input("Data da despesa").strip()
    
    # Formata automaticamente para dd/mm/aaaa se tiver 8 números
    if len(data_input) == 8 and data_input.isdigit():
        data = f"{data_input[0:2]}/{data_input[2:4]}/{data_input[4:8]}"
    else:
        data = data_input  
        # Mantém como o usuário digitou se ele preferir colocar as barras
    
    despesa = {
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor,
        "data": data
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