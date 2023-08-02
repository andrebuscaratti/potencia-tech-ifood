from datetime import datetime

print('Olá! Seja bem vindo.\nPor favor, selecione uma das opções abaixo.')

menu = """
====== MENU ======

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

==================
"""
data_hora_atual = datetime.now()
data_hora_formatado = data_hora_atual.strftime('%d/%m/%Y %H:%M')
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.upper() == 'D':
        quantia = float(input('Perfeito!\nQuanto deseja depositar?:'))
        if quantia <= 0:
            print('Valor inválido, tente novamente.')
        else:
            saldo += quantia
            print(f'Depósito realizado, seu saldo atual é de: R$ {saldo:.2f}')
            extrato.append(f'Depósito realizado em: {data_hora_formatado} | no valor de +R$ {quantia:.2f}')

    elif opcao.upper() == 'S':
        saque = float(input('Perfeito!\nQuanto deseja sacar?:'))
        if saque <= 0:
            print('Valor inválido, tente novamente.')
        elif saque > saldo:
            print('Saldo insuficiente, tente novamente.')
        elif saque > limite:
            print('O saque excede o limite de R$500,00 por transação, tente novamente.')
        elif numero_saques == LIMITE_SAQUES:
            print('Numero de saques diários excedido, tente novamente amanhã..')
        else:
            saldo -= saque
            numero_saques += 1
            print(f'Saque realizado, seu saldo atual é de: R$ {saldo:.2f}')
            extrato.append(f'Saque realizado em: {data_hora_formatado} | no valor de -R$ {saque:.2f}')

    elif opcao.upper() == 'E':
        if extrato == []:
            print('Extrato vazio. Realiza uma transação e ela aparecerá aqui.')
        else:
            print(f'Saldo atual: R$ {saldo:.2f}\n')
            for i in extrato:
                print(i)
    elif opcao.upper() == 'Q':
        break
    else:
        print('Opção inválida, tente novamente.')





