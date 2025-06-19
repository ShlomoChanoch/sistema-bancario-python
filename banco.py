# Importando as bibliotecas necessárias
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe Pessoa Física
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

# Classe Conta
class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0.0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self.data_criacao = datetime.now()

    @classmethod
    def criar_conta(cls, numero_conta, cliente):
        return cls(numero_conta, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            return True
        else:
            print('Operação falhou! O valor informado é inválido.')
            return False

    def sacar(self, valor):
        if valor > self.saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif valor <= 0:
            print('Operação falhou! O valor do saque deve ser positivo.')
        else:
            self._saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            return True
        return False

    def exibir_extrato(self):
        transacoes = self.historico.transacoes
        if not transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}")
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")


# Classe para Conta Corrente
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saques.__name__]
        )
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print(f'Operação falhou! O valor máximo para saque é R$ {self._limite:.2f}.')
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido.')
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"Agência: {self.agencia}\nConta Corrente: {self.numero_conta}\nCliente: {self.cliente.nome}"

# Classe de Históricos de Movimentação
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

# Classe de Transações
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saques(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

# Classe Depositos
class Depositos(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


# Funções do Menu

def menu():
    menu_text = """
    [n] Nova conta
    [c] Cadastrar cliente
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
    => """
    return input(menu_text).strip().lower()

def filtrar_cliente(cpf, usuarios):
    clientes_filtrados = [cliente for cliente in usuarios if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!")
        return None
    return cliente.contas[0]

def depositar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Depositos(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.transacao(conta, transacao)

def sacar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saques(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.transacao(conta, transacao)

def exibir_extrato(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\nCliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    conta.exibir_extrato()

def criar_cliente(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, usuarios)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/Estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    usuarios.append(cliente)
    print("\nCliente criado com sucesso!")

def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, usuarios)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.criar_conta(cliente=cliente, numero_conta=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("\nConta criada com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print(str(conta))

# Loop Principal
def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "n":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)
        elif opcao == "c":
            criar_cliente(usuarios)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "d":
            depositar(usuarios)
        elif opcao == "s":
            sacar(usuarios)
        elif opcao == "e":
            exibir_extrato(usuarios)
        elif opcao == "x":
            print('Saindo do sistema...')
            break
        else:
            print("\nOperação inválida! Por favor, selecione uma opção válida.")

main()