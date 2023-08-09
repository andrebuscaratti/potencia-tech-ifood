from datetime import datetime
import textwrap

def menu():
    menu = f"""
====================
Escolha uma das opções abaixo:

[D]  Depositar
[S]  Saque
[E]  Extrato
[NU] Novo Cliente
[LU] Listar Cliente
[NC] Nova Conta
[LC] Listar Conta
[Q]  Sair

====================
"""
    opcao_menu = input(menu)
    return opcao_menu


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, data_hora_formatado):
    saldo_insuficiente = valor > saldo
    saque_limite = valor > limite
    numero_saques_excedido = (numero_saques == limite_saques)
    if saldo_insuficiente:
        print('Saldo insuficiente, tente novamente.')
    elif saque_limite:
        print('O saque excede o limite de R$500,00 por transação, tente novamente.')
    elif numero_saques_excedido:
        print('Numero de saques diários excedido, tente novamente amanhã..')
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        print(f'Saque realizado, seu saldo atual é de: R$ {saldo:.2f}')
        extrato.append(f'Saque realizado em: {data_hora_formatado} | no valor de R$ {valor:.2f}')
    else:
        print('Valor inválido!')

    return numero_saques, saldo, extrato

def depositar(saldo, valor, extrato, data_hora_formatado):
    valor_invalido = valor <= 0
    if valor_invalido:
        print('Valor inválido, tente novamente.')
    else:
        saldo += valor
        print(f'Depósito realizado, seu saldo atual é de: R$ {saldo:.2f}')
        extrato.append(f'Depósito realizado em: {data_hora_formatado} | no valor de R$ {valor:.2f}')
        return saldo, extrato


def mostrar_extrato(saldo, *, extrato):
    print(f'Saldo atual: R$ {saldo:.2f}\n')
    for i in extrato:
        print(i)


def criar_cliente(clientes):
    cpf = input('CPF (somente número):')
    cliente = filtrar_clientes(cpf, clientes)
    if cliente:
        print('Cliente já cadastrado!')
    else:
        nome = input("Nome completo: ")
        data_nasc = input("Data de nascimento: ")
        logradouro = input("Logradouro: ")
        num = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        endereco = f'{logradouro}, {num} - {bairro} - {cidade}/{estado}'
        clientes.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})


def listar_cliente(clientes):
    for cliente in clientes:
        linha = f"""\
            Nome:\t{cliente['nome']}
            CPF:\t{cliente['cpf']}
            Data de Nascimento:\t{cliente['data_nasc']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def criar_conta(agencia, numero_conta, clientes):
    cpf = input('CPF (somente número):')
    cliente = filtrar_clientes(cpf, clientes)
    if cliente:
        print('Conta criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cliente}
    else:
        print('Cliente não encontrado, encerrando processo de criação de conta...')


def listar_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def main():
    AGÊNCIA = '0001'
    clientes = []
    contas = []
    data_hora_atual = datetime.now()
    data_hora_formatado = data_hora_atual.strftime('%d/%m/%Y %H:%M')
    saldo = 20
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3


    while True:
        opcao_menu = menu()

        if opcao_menu.upper() == 'D':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(valor, saldo, extrato, data_hora_formatado)
        elif opcao_menu.upper() == 'S':
            valor = float(input('Informe o valor do saque: '))
            numero_saques, saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                data_hora_formatado=data_hora_formatado
            )
        elif opcao_menu.upper() == 'E':
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao_menu.upper() == 'NU':
            criar_cliente(clientes)
            print(clientes)
        elif opcao_menu.upper() == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGÊNCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)
        elif opcao_menu.upper() == 'LC':
            listar_conta(contas)
        elif opcao_menu.upper() == 'LU':
            listar_cliente(clientes)
        elif opcao_menu.upper() == 'Q':
            break
        else:
            print('Opção inválida!')


main()