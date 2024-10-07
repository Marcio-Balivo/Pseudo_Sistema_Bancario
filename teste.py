from datetime import datetime

COMPRIMENTO = 80
SAQUE_MAX = 500.0
saldo = 0.0
transacoes = 0
extrato = ""
dia_atual = datetime.strftime(datetime.now(), "%d")

menu = f'''\
{"".center(COMPRIMENTO, "=")}
{" SISTEMA BANCÁRIO ".center(COMPRIMENTO, "$")}
{"".center(COMPRIMENTO, "=")}
OPÇÕES:
1. Depositar
2. Sacar
3. Emitir Extrato

0. Sair
{"".center(COMPRIMENTO, "=")}'''

while True:
    print(menu)
    opcao = input("Informe a opção desejada: ")

    if opcao == "0":
        exit (0)

    elif opcao == "1":
        dia_transacao = datetime.strftime(datetime.now(), "%d")

        if dia_atual != dia_transacao:
            dia_atual = datetime.strftime(datetime.now(), "%d")
            transacoes = 0

        cabecalho_depositar = f'''
{"".center(COMPRIMENTO, "=")}
{" DEPOSITAR ".center(COMPRIMENTO, "+")}
{"".center(COMPRIMENTO, "=")}'''
        print(cabecalho_depositar)
        valor = float(input("Informe o valor a depositar: R$ "))

        if valor <= 0:
            print("\nO valor deve ser maior que 0(zero)!\n")

        elif transacoes == 10:
            print("\nLimite de transações diárias (10) atingido!\n")

        else:
            dia_transacao = datetime.strftime(datetime.now(), "%d")

            if dia_atual != dia_transacao:
                dia_atual = datetime.strftime(datetime.now(), "%d")
                transacoes = 0     

            saldo += valor
            transacoes += 1
            extrato += f"Depósito\t{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")}\t R$ {valor:.2f}\n"
            print("\nO depósito foi realizado!\n")

    elif opcao == "2":
        cabecalho_sacar = f'''
{"".center(COMPRIMENTO, "=")}
{" SACAR ".center(COMPRIMENTO, "-")}
{"".center(COMPRIMENTO, "=")}'''
        print(cabecalho_sacar)
        valor = float(input("Informe o valor a sacar: R$ "))

        if valor > SAQUE_MAX:
            print("\nO valor deve ser menor ou igual a R$ 500,00!\n")

        elif valor > saldo:
            print("\nO saldo disponível é insuficiente!\n")

        elif transacoes == 10:
            print("\nLimite de transações diárias (10) atingido!\n")

        else:
            dia_transacao = datetime.strftime(datetime.now(), "%d")

            if dia_atual != dia_transacao:
                dia_atual = datetime.strftime(datetime.now(), "%d")
                transacoes = 0         

            saldo -= valor
            transacoes += 1
            extrato += f"Saque\t{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")}\tR$ {valor:.2f}\n"
            print("\nO saque foi realizado!\n")

    elif opcao == "3":
        cabecalho_extrato = f'''
{"".center(COMPRIMENTO, "=")}
{" EXTRATO ".center(COMPRIMENTO, "!")}
{"".center(COMPRIMENTO, "=")}'''
        print(cabecalho_extrato)
        print(f"{extrato}{''.center(COMPRIMENTO, '=')}\nSaldo R$ {saldo:.2f}\n") if extrato else print("\nNenhuma operação foi registrada!\n")