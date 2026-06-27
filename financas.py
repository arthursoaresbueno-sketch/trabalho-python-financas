from datetime import datetime

lancamentos = []

def registrar_lancamento():
    print ("Voce esta registrando um lancamento.")

    tipo = input("Digite o tipo (receita/despesa): ").lower()
    while True:
        try:
            valor = float(input("Digite o valor: "))
            break
        except ValueError:
            print("Digite apenas numeros.")
    valor = input("Digite o valor: ")
    categoria = input("Digite a categoria: ")
    descricao = input("Digite a descricao: ")
    print("\nLancamento registrado!")

    data = datetime.now().strftime("%d/%m/%Y")
    lancamentos.append([data, tipo, valor, categoria, descricao])

def ver_extrato():
    print("\n--- EXTRATO ---")

    if len(lancamentos) == 0:
            print("Nenhum lancamento registrado.")
    else:
        for lancamento in lancamentos:
            print("---------------------------")
            print("Data:", lancamento[0])
            print("Tipo:", lancamento[1])
            print("Valor: R$", lancamento[2])
            print("Categoria:", lancamento[3])
            print("Descricao:", lancamento[4])

def relatorio():
    total_receitas = 0
    total_despesas = 0
    for lancamento in lancamentos:
        if lancamento[1] == "receita":
            total_receitas = total_receitas + float(lancamento[2])
        elif lancamento[1] == "despesa":
            total_despesas = total_despesas + float(lancamento[2])
    saldo = total_receitas - total_despesas
    print("\n---Relatorio---")
    print("Total de receitas R$:", total_receitas)
    print("Total de despesas R$:", total_despesas)
    print("Saldo R$:", saldo)

def exportar_relatorio():
    total_receitas = 0
    total_despesas = 0
    for lancamento in lancamentos:
        if lancamento[0] == "receita":
            total_receitas = total_receitas + float(lancamento[1])
        elif lancamento[0] == "despesa":
            total_despesas = total_despesas + float(lancamento[1])
    saldo = total_receitas - total_despesas

    arquivo = open("relatorio.txt", "w")

    arquivo.write("--- RELATORIO FINANCEIRO ---\n")
    arquivo.write("Total de receitas: R$ " + str(total_receitas) + "\n")
    arquivo.write("Total de despesas: R$ " + str(total_despesas) + "\n")
    arquivo.write("Saldo: R$ " + str(saldo) + "\n")

    arquivo.close()

    print("Relatorio exportado com sucesso!")


while True:

    print ("---APP DE FINANCAS---")
    print ("1- Registrar lancamentos")
    print ("2- Ver extrato")
    print ("3- Relatorio")
    print ("4- Exportar relatorio")
    print ("5- Sair")

    opcao = input ("Escolha uma opcao: ")

    if opcao == "1":
        registrar_lancamento()
    elif opcao == "2":
        ver_extrato()
    elif opcao == "3":
        relatorio()
    elif opcao == "4":
        exportar_relatorio()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print ("Opcao invalida")
