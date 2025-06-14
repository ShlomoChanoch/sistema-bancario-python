menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair
"""


saldo = 0
LIMITE = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Função para realizar o depósito
def depositar(deposito):
    global saldo
    if deposito > 0:
        saldo += deposito
        extrato.append(f'Depósito: R$ {deposito:.2f}')
        print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
        return saldo
    else:
        print('Operação falhou! O valor informado é inválido.')

# Função para realizar o saque
def sacar(saque):
    global saldo, numero_saques, LIMITE_SAQUES, LIMITE
    if saque > saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif saque > LIMITE:
        print(f'Operação falhou! O valor máximo para saque é R$ {LIMITE:.2f}.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Operação falhou! Número máximo de saques excedido.')
    else:
        saldo -= saque
        extrato.append(f'Saque: R$ {saque:.2f}')
        numero_saques += 1
        print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
    return saldo

# Função para exibir o extrato bancário
def exibir_extrato():
    if not extrato:
        print('Não foram realizadas movimentações.')
    else:
        print('Extrato:')
        for operacao in extrato:
            print(operacao)
        print(f'Saldo atual: R$ {saldo:.2f}')

# Loop principal do sistema bancário
while True:
    opcao = input(menu).strip().lower()

    if opcao == 'd':
        deposito = float(input('Informe o valor do depósito: '))
        depositar(deposito)
    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))
        sacar(saque)
    elif opcao == 'e':
        exibir_extrato()
    elif opcao == 'x':
        print('Saindo do sistema...')
        break
    else:
        print('Operação inválida! Por favor, selecione uma opção válida.')