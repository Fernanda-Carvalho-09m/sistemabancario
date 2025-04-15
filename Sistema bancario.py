"""
1 - Criar um sistema bancário com operações: sacar, depositar e visualizar extrato. 

2 - Deve ser possível depositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma 
não precisamos nos preocupar em identificar qual é o número da agência e conta bancária, Todos os depósitos devem ser armazenados em 
uma variável exibidos na operação extrato.

3 - O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha saldo em conta, o
sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados
em uma variável e exibidos na operação de extrato.

4 - Essa operação deve listar todos os depósito e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
Os valores devem ser exibidos utilizando o formado R$ xxx.xx, exemplo: 1500.45 - R$ 1500.45

 """


menu = """


[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print("Valor de depósito deve ser positivo.")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: R$ "))
        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo and valor <= limite:
                saldo -= valor
                extrato.append(f'Saque: R$ {valor:.2f}')
                numero_saques += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            elif valor > saldo:
                print('Saldo insuficiente para realizar o saque.')
            else:
                print('O valor do saque deve ser no máximo R$ 500,00.')
        else:
            print('Limite de saques diários atingido.')

    elif opcao == "3":
        print("\n=== Extrato Bancário ===")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in extrato:
                print(movimento)
        print(f'Saldo atual: R$ {saldo:.2f}')
        print("=========================\n")

    elif opcao == "4":
        print("Saindo do sistema...")
        break 

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")