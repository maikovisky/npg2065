
# Classe cliente
class Cliente:
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

class Conta:
	def __init__(self, numero, saldo):
		self.numero = numero
		self.saldo = saldo

	def saldo(self):
		print("Saldo:" + self.saldo)

	def deposito(self, valor):
		self.saldo = self.saldo + valor

	def saque(self, valor):
		self.saldo = self.saldo - valor

class ContaEspecial(Conta):
	def __init__(self, numero, saldo, limite):
		self.numero = numero
		self.saldo = saldo
		self.limite = limite

	def saldo(self):
		print("Limite: " + self.limite)
		print("Saldo.: " + self.saldo)


cli = Cliente("Maiko", "99119919")
conta = Conta("1234", 0.00)

