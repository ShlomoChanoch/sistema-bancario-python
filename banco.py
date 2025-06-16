# Função para exibir o menu de opções
def menu():
    menu_text = """
    [n] Nova conta
    [c] Cadastrar cliente
    [l] Listar clientes
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
    """
    return input(menu_text).strip().lower()

# Função principal do sistema bancário
def main():
    saldo = 0
    LIMITE = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == 'n':
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 'c':
            cadastrar_cliente(usuarios)
        elif opcao == 'l':
            listar_clientes(usuarios)
            listar_contas(contas)
        elif opcao == 'd':
            deposito = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, deposito, extrato)
        elif opcao == 's':
            saque = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                LIMITE=LIMITE,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'x':
            print('Saindo do sistema...')
            break
        else:
            print('Operação inválida! Por favor, selecione uma opção válida.')


# Função para realizar o depósito
def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato.append(f'Depósito: R$ {deposito:.2f}')
        print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
        return saldo, extrato
    else:
        print('Operação falhou! O valor informado é inválido.')

# Função para realizar o saque
def sacar(*, saldo, saque, extrato, LIMITE, numero_saques, LIMITE_SAQUES):
    if saque > saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif saque > LIMITE:
        print(f'Operação falhou! O valor máximo para saque é R$ {LIMITE:.2f}.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Operação falhou! Número máximo de saques excedido.')
    elif saque > 0:
        saldo -= saque
        extrato.append(f'Saque: R$ {saque:.2f}')
        numero_saques += 1
        print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
    return saldo, extrato, numero_saques

# Função para exibir o extrato bancário
def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print('Não foram realizadas movimentações.')
    else:
        print('Extrato:')
        for operacao in extrato:
            print(operacao)
        print(f'Saldo atual: R$ {saldo:.2f}')

# Função para cadastrar cliente
def cadastrar_cliente(usuarios):
    cpf = input("Digite aqui o CPF do cliente (somente números):\n")
    usuario = filtrar_cliente(cpf, usuarios)
    if usuario:
        print(f"Cliente {usuario['nome']} já cadastrado com CPF {usuario['cpf']}.")
        return
    else:
        nome = input("Digite aqui o nome completo do cliente:\n")
        data_nascimento = input("Digite aqui a data de nascimento do cliente (DD/MM/AAAA):\n")
        endereco = input("Digite aqui o endereço do cliente (logradouro, número - bairro - Cidade/Estado):\n")

        usuarios.append({
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        })
        print(f"Cliente {nome} com CPF {cpf} cadastrado com sucesso!")

# Função para cadastrar conta bancária
def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do cliente para vincular à conta:\n")
    usuario = filtrar_cliente(cpf, usuarios)
    if usuario:
        print(f"Conta criada com sucesso para o cliente {usuario['nome']}!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    else:
        print("Cliente não encontrado. Por favor, cadastre o cliente primeiro.")
        return None

# Função para filtrar cliente pelo CPF
def filtrar_cliente(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para listar clientes cadastrados
def listar_clientes(usuarios):
    if not usuarios:
        print("Nenhum cliente cadastrado.")
    else:
        print("Clientes cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Data de Nascimento: {usuario['data_nascimento']}, Endereço: {usuario['endereco']}")

# Função para listar contas bancárias
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("Contas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Cliente: {conta['usuario']['nome']}")

if __name__ == "__main__":
    main()