import json

ARQUIVO_DADOS = "despesas.json"

def carregar_despesas():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_despesas(lista_despesas):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(lista_despesas, f, ensure_ascii=False, indent=4)

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
    data_input = input("Data da despesa: ").strip()
    
    # Formata automaticamente para dd/mm/aaaa se tiver 8 números
    if len(data_input) == 8 and data_input.isdigit():
        data = f"{data_input[0:2]}/{data_input[2:4]}/{data_input[4:8]}"
    else:
        data = data_input  # Mantém como o usuário digitou
    
    despesa = {
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor,
        "data": data
    }

    return despesa

def listar_despesas(despesas):
    print("\n========== DESPESAS REGISTRADAS ==========")
    if not despesas:
        print("Nenhuma despesa cadastrada ainda.")
        return
        
    for i, despesa in enumerate(despesas):
        # Usamos i + 1 para o usuário ver de 1 em diante, mas lembre-se que na lista o índice real é `i`
        print(f"\n[{i+1}] Descrição: {despesa['descricao']}")
        print(f"    Categoria: {despesa['categoria']}")
        print(f"    Valor: R$ {despesa['valor']:.2f}")
        print(f"    Data: {despesa['data']}")


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

def remover_despesas(despesas):
    if not despesas:
        print("\n❌ Não há despesas para remover.")
        return

    listar_despesas(despesas)
    
    while True:
        try:
            numero_escolhido = int(input("\nDigite o número da despesa que deseja remover: "))
            indice = numero_escolhido - 1
            
            # 1. Primeiro validamos se o índice existe
            if 0 <= indice < len(despesas):
                # 2. Se existe, pedimos a confirmação antes de apagar de vez
                confirmacao = input(f"Tem certeza que deseja apagar a despesa '{despesas[indice]['descricao']}'? (s/n): ").strip().lower()
                
                if confirmacao == "s":
                    removida = despesas.pop(indice)
                    salvar_despesas(despesas)
                    print(f"🗑️ Despesa '{removida['descricao']}' removida com sucesso!")
                    break
                elif confirmacao == "n":
                    print("❌ Operação cancelada. A despesa não foi apagada.")
                    break
                else:
                    print("❌ Opção inválida. Digite 's' para sim ou 'n' para não.")
                    break # ou podemos deixar o usuário tentar digitar a confirmação de novo
            else:
                print("❌ Número inválido! Escolha um número que apareça na lista acima.")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")

# PROGRAMA PRINCIPAL

print("================================")
print("       EXPENSE TRACKER")
print("Bem-vindo ao seu controle de gastos!")
print("================================")

# 1. Carrega as despesas salvas anteriormente (se houverem)
despesas = carregar_despesas()

while True:
    print("\n=== MENU ===")
    print("1. Cadastrar nova despesa")
    print("2. Listar despesas e resumo")
    print("3. Remover despesa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        despesa = cadastrar_despesa()
        despesas.append(despesa)
        salvar_despesas(despesas)
        print("💾 Despesa salva com sucesso no arquivo!")
        
    elif opcao == "2":
        listar_despesas(despesas)
        mostrar_resumo(despesas)
        
    elif opcao == "3":
        remover_despesas(despesas)
        
    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break 
    else:
        print("Opção inválida! Tente novamente.")