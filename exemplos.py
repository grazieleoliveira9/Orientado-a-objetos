class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo 

    def depositar(self, valor):
        self.saldo += valor

    def sacar (self, valor):
        self.saldo -= valor 

    def gerar_extrato(self):
        print(f'numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}')


def main():
    c1= Conta(1,1,"João", 0) # Objeto sendo instanciado
    #print(f'Nome do titular da conta: {c1.nomeTitular}')
    #print(f'Número da conta: {c1.numero}')
    #print(f'CPF do titular da conta: {c1.cpf}')
    #print(f'Saldo da conta: {c1.saldo}')


# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    c1.sacar(100)
    c1.gerar_extrato()

if __name__ == "__main__": 
    main()