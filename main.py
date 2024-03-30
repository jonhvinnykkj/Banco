from banco import conta, salvar_conta
import random

#input que pede as opçoes para a pessoa, 1 - criar conta / 2 - acessar conta
opcao = int(input("[ 1 ] para criar uma conta\n[ 2 ] para acessar uma conta existente: "))
#verifica se a opção é valida
if opcao != 1 and opcao != 2:
    print("Opção inválida!")
    exit()
    
#verifica se a opção é 1
if opcao == 1:
    nome = input("Digite seu nome: ")
#verifica se o nome é numerico
    if nome.isnumeric():
        print("Nome inválido!")
        exit()
        
    cpf = input("Digite seu CPF:(Sem ""-"" ou ""."") ")
    
    #verifica se o cpf ja existe
    with open("conta.csv", "r") as file:
        for linha in file:
            dados_conta = linha.strip().split(",")
            if cpf == dados_conta[1]:
                print("CPF já existente!")
                exit()
                
    #verifica se o cpf é valido
    # #if len(cpf) != 11:
    #     print("CPF inválido!")
    #     exit()
    #verifica se o cpf é numerico
    if not cpf.isnumeric():
        print("CPF inválido!")
        exit()
                
    idade = input("Digite sua idade: ")
    #verifica se a idade é numerica
    if not idade.isnumeric():
        print("Idade inválida!")
        exit()
    #verifica se a idade é valida
    if not idade.isnumeric():
        print("Idade inválida!")
        exit()

    #verifica se a idade é maior que 18
    if int(idade) < 18:
        print("Apenas maiores de 18 anos podem criar uma conta!")
        exit()
        
    #cria uma conta aleatoria de 0000 a 9999
    numero_conta = str(random.randint(0, 9999)).zfill(4)
    
    #verifica se a conta ja existe, se existir, gera outra conta e assim infinitamente
    with open("conta.csv", "r") as file:
        for linha in file:
            dados_conta = linha.strip().split(",")
            if numero_conta == dados_conta[3]:
                numero_conta = str(random.randint(0, 9999)).zfill(4)
                break
        else:
            pass
#define como saldo inicial da conta como 100 no aquivo csv
    conta1 = conta(nome, cpf, idade, numero_conta, 100)
    salvar_conta(conta1)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}, e seu saldo inicial é de R$100,00.")
else:
    numero_conta = input("Digite o número da conta: ")
    with open("conta.csv", "r") as file:
        for linha in file:
            dados_conta = linha.strip().split(",")
            if numero_conta == dados_conta[3]:
                conta1 = conta(dados_conta[0], dados_conta[1], dados_conta[2], dados_conta[3], float(dados_conta[4]))
                break
        else:
            print("Conta não encontrada!")
            exit()
    while True:
        print("Escolha uma opção:\n1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Transferência\n5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            conta1.deposito(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            conta1.saque(valor)
            salvar_conta(conta1)
        elif opcao == 3:
            conta1.extrato()
            
        elif opcao == 4:
            numero_conta_destino = input("Digite o número da conta de destino: ")
            with open("conta.csv", "r") as file:
                for linha in file:
                    dados_conta = linha.strip().split(",")
                    conta_destino = conta(dados_conta[0], dados_conta[1], dados_conta[2], dados_conta[3], float(dados_conta[4]))
                    if numero_conta_destino == conta_destino.numero_conta:
                        break
                else:
                    print("Conta de destino não encontrada!")
                    continue
            valor = float(input("Digite o valor da transferência: "))
                
            conta1.transferencia(valor, conta_destino)
        else:
            break