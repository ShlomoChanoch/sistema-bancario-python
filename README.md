# Sistema Bancário no Python

Neste projeto proposto pela [DIO](dio.me), criei um Sistema Bancário em Python.

O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema é desenvolvido para um banco fictício que busca monetizar suas operações. Durante o desafio, apliquei meus conhecimentos em programação Python e criei um sistema funcional que simula operações bancárias.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja monetizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema, devemos implementar apenas 3 operações: depósito, saque e extrato.

## 1. Operação de Depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual o número da agência e da conta bancária.

Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## 2. Operação de Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.

Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem de que não será possível realizar o saque por falta de dinheiro.

Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## 3. Operação de Extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

1500.45 = R$ 1500.45