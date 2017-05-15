import sys
import os
# Classe cliente
class Cliente:
	def __init__(self, nome, telefone):
		self.contas = []
		self.nome = nome
		self.telefone = telefone
	
	def addConta(self, conta)
		self.contas.appenf(conta)

class Clientes:
	def __init__(self)
		self.lista = []

	def addCliente(self, cliente)
		self.lista.append(cliente)

class Movimentacao:
	def __init__(self, operacao, valor):
		if ( operacao == "S" ):
			self.operacao = "SAQUE"
			self.valor = valor * -1
		else:
			self.operacao = "DEPOSITO"
			self.valor = valor 

	def __str__(self):
		return "{0:22s} {1:10.2f}".format(self.operacao, self.valor)

class Conta:
	def __init__(self, numero, cliente):
		self.movimentacoes = []
		self.numero = numero
		self.cliente = cliente

	def saldo(self):
		valor = 0
		for m in self.movimentacoes:
			valor = valor + m.valor

		return valor

	def extrato(self):
		print("*********** EXTRATO *************")
		print("Extrato da conta numero: " + self.numero)
		valor = 0
		for m in self.movimentacoes:
			valor = valor + m.valor
			print(m)
		print "{0:22s} {1:10.2f}".format("SALDO", valor)
		print("*********************************")

		

	def deposito(self, valor):
		m = Movimentacao("D", valor)
		self.movimentacoes.append(m)

	def saque(self, valor):
		m = Movimentacao("S", valor)
		self.movimentacoes.append(m)

class ContaEspecial(Conta):
	def __init__(self, numero, saldo, limite):
		self.numero = numero
		self.saldo = saldo
		self.limite = limite

	def saldo(self):
		print("Limite: " + self.limite)
		print("Saldo.: " + self.saldo)

def addCliente:
	

# Mostra o menu
def exibirMenu():
	print("1 - Cadastro de Cliente")
	print("2 - Cadastro de Conta")
	print("3 - Deposito")
	print("4 - Saque")
	print("5 - Extrato")
	print("0 - Sair")
	option = int(input("Escolha uma opcao: "))
	return option

cto = Conta("1234")

while True:
	op = exibirMenu()
	if (op == 0):
		print("Fim do Programa")
		break
	elif (op == 1):
		pass
	elif (op == 2):
		pass
	elif (op == 3):
		conta = input("Numero da conta para deposito: ")
		cto.deposito(float(input("Valor do deposito: ")))
	elif (op == 4):
		conta = input("Numero da conta para saque: ")
		cto.saque(float(input("Valor do saque: ")))
	elif (op == 5):
		conta = input("Numero da conta para extrato: ")
		cto.extrato()
	else:
		print("Opcao invalida")
	


