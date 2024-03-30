import csv
class clientes:
    def __init__(self, nome, cpf, idade, numero_conta, saldo):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.numero_conta = numero_conta
        self.saldo = saldo

class conta(clientes):
    def deposito(self, valor):
        # verifica se o valor é maior que 0
        if valor <= 0:
            print("Valor inválido!\n")
            return
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso! Saldo atual: R${self.saldo}\n")
        salvar_conta(self, valor)  # apenas uma chamada para salvar_conta

    def saque(self, valor):
        # verifica se o valor é maior que 0
        if valor <= 0:
            print("Valor inválido!\n")
            return
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso! Saldo atual: R${self.saldo}\n")
            salvar_conta(self,valor)  # apenas uma chamada para salvar_conta
        else:
            print("Saldo insuficiente!\n")
            
    def extrato(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\nNúmero da conta: {self.numero_conta}\nSaldo: R${self.saldo}\n")  

# função de transferencia que altera o valor atual da conta e o da conta de destino no arquivo CSV
    def transferencia(self, valor, conta_destino):
        if valor <= 0:
            print("Valor inválido!\n")
            return
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor} realizada com sucesso! Saldo atual: R${self.saldo}\n")
            salvar_conta(self, valor, conta_destino)  # apenas uma chamada para salvar_conta    
        else:
            print("Saldo insuficiente!\n")
            
#Armazana as contas em um arquivo CSV ja existente. #se o dado ja existir no arquivo csv, apenas reescrever ele substituido-o
def salvar_conta(conta, valor):
    with open("conta.csv", "r") as file:
        dados = file.readlines()
    with open("conta.csv", "w") as file:
        writer = csv.writer(file)
        #writer.writerow(["Nome", "CPF", "Idade", "Número da conta", "Saldo"])
        conta_existente = False
        for linha in dados:
            dados_conta = linha.strip().split(",")
            if conta.numero_conta == dados_conta[3]:
                writer.writerow([conta.nome, conta.cpf, conta.idade, conta.numero_conta, conta.saldo])
                conta_existente = True
            else:
                writer.writerow(dados_conta)
        if not conta_existente:
            writer.writerow([conta.nome, conta.cpf, conta.idade, conta.numero_conta, conta.saldo])