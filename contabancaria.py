class clientes: 
    def CPF  ( nome, numero):
        input (f"faça seu cadastro insira seu {"CPF(nome, numero)"}")

class ContaBancaria:
        total_contas = 0
        taxa_juros = 0.0
    
        def __init__(self, titular, saldo_inicial=0):

            self.titular = titular
            self.saldo = saldo_inicial
            ContaBancaria.total_contas += 1

        def depositar(self, valor):
            self.saldo += valor
            print(f"{valor} depositados. Saldo atual: {self.saldo}")

        def sacar(self, valor):
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"{valor} sacados. Saldo atual: {self.saldo}")
            else:
                print("Saldo insuficiente para saque.")

        def verificar_saldo(self):
            print(f"Saldo de {self.titular}: {self.saldo}")
            return self.saldo
        
        @classmethod
        def ajustar_taxa_juros(cls, nova_taxa):
            cls.taxa_juros = nova_taxa
            print(f"Nova taxa de juros ajustada para: {cls.taxa_juros * 100}% ao ano.")

        @classmethod
        def mostrar_total_contas(cls):
            print(f"Total de contas bancárias criadas: {cls.total_contas}")

        @staticmethod
        def converter_moeda(valor, taxa_conversao):
            return valor * taxa_conversao

        @staticmethod
        def dias_no_ano():
            return 365

conta1 = ContaBancaria("Maria", 1000)
conta2 = ContaBancaria("João", 500)

conta1.depositar(200)
conta2.sacar(100)
conta1.verificar_saldo()
conta1.verificar_saldo()

ContaBancaria.ajustar_taxa_juros(0.07)
ContaBancaria.mostrar_total_contas()

valor_convertido = ContaBancaria.converter_moeda(100, 5.2)
print(f"Valor convertido: {valor_convertido}")

dias = ContaBancaria.dias_no_ano()
print(f"Número de dias no ano: {dias}")
