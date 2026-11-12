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

    while True:
        try:
            valor_str = input("Valor da despesa: ").replace(',', '.')
            valor = float(valor_str)
            break
        except ValueError:
            print("❌ Valor inválido! Digite apenas números (use ponto para decimais).")

    data_input = input("Data da despesa: ").strip()
    
    if len(data_input) == 8 and data_input.isdigit():
        data = f"{data_input[0:2]}/{data_input[2:4]}/{data_input[4:8]}"
    else:
        data = data_input 
    
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
            
            if 0 <= indice < len(despesas):
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
            else:
                print("❌ Número inválido! Escolha um número que apareça na lista acima.")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")

def editar_despesas(despesas):
    if not despesas:
        print("\n❌ Não há despesas para editar.")
        return

    listar_despesas(despesas)
    
    while True:
        try:
            numero_escolhido = int(input("\nDigite o número da despesa que deseja editar: "))
            indice = numero_escolhido - 1
            
            if 0 <= indice < len(despesas):
                despesa_atual = despesas[indice]
                print(f"\nEditando a despesa: '{despesa_atual['descricao']}'")
                print("Dica: Se quiser manter o valor atual, basta pressionar Enter sem digitar nada.")
                
                # atualiza descrição
                nova_descricao = input(f"Nova descrição [{despesa_atual['descricao']}]: ").strip()
                if nova_descricao:
                    despesa_atual['descricao'] = nova_descricao
                
                # atualiza categoria
                nova_categoria = input(f"Nova categoria [{despesa_atual['categoria']}]: ").strip()
                if nova_categoria:
                    despesa_atual['categoria'] = nova_categoria
                
                # atualizando valor com tratamento de erro
                novo_valor_str = input(f"Novo valor [R$ {despesa_atual['valor']:.2f}]: ").replace(',', '.').strip()
                if novo_valor_str:
                    try:
                        despesa_atual['valor'] = float(novo_valor_str)
                    except ValueError:
                        print("❌ Valor inválido! O valor anterior foi mantido.")

                # atualiza data
                nova_data = input(f"Nova data [{despesa_atual['data']}]: ").strip()
                if nova_data:
                    if len(nova_data) == 8 and nova_data.isdigit():
                        despesa_atual['data'] = f"{nova_data[0:2]}/{nova_data[2:4]}/{nova_data[4:8]}"
                    else:
                        despesa_atual['data'] = nova_data

                # isso salva as alterações no JSON
                salvar_despesas(despesas)
                print("💾 Despesa atualizada com sucesso!")
                break
            else:
                print("❌ Número inválido! Escolha um número que apareça na lista acima.")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")

# PROGRAMA PRINCIPAL

print("================================")
print("       EXPENSE TRACKER")
print("Bem-vindo ao seu controle de gastos!")
print("================================")

despesas = carregar_despesas()

while True:
    print("\n=== MENU ===")
    print("1. Cadastrar nova despesa")
    print("2. Listar despesas e resumo")
    print("3. Remover despesa")
    print("4. Editar despesa")
    print("5. Sair")

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
        editar_despesas(despesas)
        
    elif opcao == "5":
        print("Saindo do programa. Até mais!")
        break 
    else:
        print("Opção inválida! Tente novamente.")