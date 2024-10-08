'''
Desafio: Otimizando o Sistema Bancário com Funções
Criar funções para criar usuário, criar conta corrente, saque, depósito e extrato.

Requisitos da função de saque:
- Parâmetros apenas kwargs;
- Sugestão de parâmetros: saldo, valor, extrato, limite, numero_saques, limite_saques.
- Sugestão de retorno: saldo e extrato.

Requisitos da função de depósito:
- Parâmetros apenas por posição;
- Sugestão de parâmetros: saldo, valor, extrato.
- Sugestão de retorno: saldo e extrato.

Requisitos da função de extrato:
- Parâmetros: saldo apenas por posição, extrato apenas keyword;


Requisitos da função criar usuário:
- Usuários devem ser armazenados numa lista;
- Dados dos usuários: nome, nascimento, cpf, endereço(logradouro, número - bairro - cidade/uf);
- Armazenar apenas os números do CPF;
- 1 usuário por CPF.

Requisitos da função criar conta corrente:
- Contas devem ser armazenadas numa lista;
- Dados da conta: número (sequencial), agencia (0001), cpf;
- Armazenar apenas os números do CPF;
- Cada conta deve estar vinculada a apenas um cliente;
- Cada cliente pode ter várias contas.

'''
from datetime import datetime

COMPRIMENTO = 80
SAQUE_MAX = 500.0
AGENCIA = "0001"
saldo = 0.0
transacoes = 0
extrato = ""
dia_atual = datetime.strftime(datetime.now(), "%d")
clientes = []
contas = []
ultima_conta = 0
menu = f'''\
{"".center(COMPRIMENTO, "=")}
{" SISTEMA BANCÁRIO ".center(COMPRIMENTO, "$")}
{"".center(COMPRIMENTO, "=")}
OPÇÕES:
1. Depositar
2. Sacar
3. Emitir Extrato
4. Cadastrar Cliente
5. Listar Clientes
6. Cadastrar Conta
7. Listar Contas

0. Sair
{"".center(COMPRIMENTO, "=")}'''

def depositar(transacoes, dia_atual, saldo, extrato,/):
    cabecalho_depositar = f'''
{"".center(COMPRIMENTO, "=")}
{" DEPOSITAR ".center(COMPRIMENTO, "+")}
{"".center(COMPRIMENTO, "=")}'''

    print(cabecalho_depositar)

    valor = float(input("Informe o valor a depositar: R$ "))

    if valor <= 0:
        print("\nO valor deve ser maior que 0 (zero)!\n")

    elif transacoes == 10:
        print("\nLimite de transações diárias (10) atingido!\n")

    else:
        dia_transacao = datetime.strftime(datetime.now(), "%d")

        if dia_atual != dia_transacao:
            dia_atual = datetime.strftime(datetime.now(), "%d")
            transacoes = 0     

        saldo += valor
        transacoes += 1
        extrato += f"Depósito\t{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")}\tR$ {valor:10.2f}\n"
        print("\nO depósito foi realizado!\n")
        return saldo, extrato, transacoes, dia_atual

def sacar(transacoes, dia_atual, saldo, extrato):
        cabecalho_sacar = f'''
{"".center(COMPRIMENTO, "=")}
{" SACAR ".center(COMPRIMENTO, "-")}
{"".center(COMPRIMENTO, "=")}'''
        print(cabecalho_sacar)
        valor = float(input("Informe o valor a sacar: R$ "))

        if valor > SAQUE_MAX:
            print("\nO valor deve ser menor ou igual a R$ 500,00!\n")

        elif valor <= 0:
            print("\nO valor deve ser maior que 0 (zero)!\n")

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
            extrato += f"Saque\t\t{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")}\tR$ {valor:10.2f}\n"
            print("\nO saque foi realizado!\n")
            return saldo, extrato, transacoes, dia_atual

def emitir_extrato(extrato, /, *, saldo):
        cabecalho_extrato = f'''
{"".center(COMPRIMENTO, "=")}
{" EXTRATO ".center(COMPRIMENTO, "!")}
{"".center(COMPRIMENTO, "=")}'''
        print(cabecalho_extrato)
        print(f"{extrato}{''.center(COMPRIMENTO, '=')}\nSaldo\t\t\t\t\tR$ {saldo:10.2f}\n") if extrato else print("\nNenhuma operação foi registrada!\n")

def cadastrar_cliente(clientes):
    cabecalho_cadastrar_cliente = f'''
{"".center(COMPRIMENTO, "=")}
{" CADASTRAR CLIENTE ".center(COMPRIMENTO, "+")}
{"".center(COMPRIMENTO, "=")}'''
    print(cabecalho_cadastrar_cliente)

    nome = input("Nome: ")
    cpf = input("CPF (apenas números): ")
    nascimento = input("Data de nascimento (dia/mês/ano): ")
    endereco = input("Endereço (logradouro, nº, bairro - cidade/UF): ")

    if not busca_valor(clientes, "cpf", cpf):
        clientes.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
        return clientes
    else:
        print("\nJá existe um cliente com o CPF informado!\n")

def busca_valor(lista, chave, valor):
    for indice, cliente in enumerate(lista):
        if lista[indice][chave] == valor:
            return True
    else:
        return False

def cadastrar_conta(contas, agencia, ultima_conta, clientes):
    cabecalho_cadastrar_conta = f'''
{"".center(COMPRIMENTO, "=")}
{" CADASTRAR CONTA ".center(COMPRIMENTO, "+")}
{"".center(COMPRIMENTO, "=")}'''
    print(cabecalho_cadastrar_conta)

    cpf = input("CPF (apenas números): ")

    if busca_valor(clientes, "cpf", cpf):
        ultima_conta += 1
        contas.append({"agencia": agencia, "conta": ultima_conta, "cpf": cpf})
        return ultima_conta, contas
    else:
        print("\nNão existe cliente com o CPF informado!\n")
    
while True:
    print(menu)
    opcao = input("Informe a opção desejada: ")

    if opcao == "0":
        exit (0)

    elif opcao == "1":
        resposta = depositar(transacoes, dia_atual, saldo, extrato)
        if resposta:             
            saldo, extrato, transacoes, dia_atual = resposta[0], resposta[1], resposta[2], resposta[3]

    elif opcao == "2":
        resposta = sacar(transacoes=transacoes, dia_atual=dia_atual, saldo=saldo, extrato=extrato)
        if resposta:
            saldo, extrato, transacoes, dia_atual = resposta[0], resposta[1], resposta[2], resposta[3]

    elif opcao == "3":
        emitir_extrato(extrato, saldo=saldo)

    elif opcao == "4":
        resposta = cadastrar_cliente(clientes)
        if resposta:
            clientes = resposta

    elif opcao == "5":
        print(f"\n{clientes}\n")

    elif opcao == "6":
        resposta = cadastrar_conta(contas, AGENCIA, ultima_conta, clientes)
        if resposta:
            ultima_conta, contas = resposta[0], resposta[1]

    elif opcao == "7":
        print(f"\n{contas}\n")