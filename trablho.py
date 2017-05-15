import sys
import os

clear = lambda: os.system('clear')

# Classe cliente
class Cliente:
	def __init__(self, nome, telefone):
		self.contas = []
		self.nome = nome
		self.telefone = telefone
	
	def add(self, conta):
		self.contas.append(conta)

	def procura(self, numero):
		for c in self.contas:
			if(c.numero == numero):
				return c
		return None

class Clientes:
	def __init__(self):
		self.lista = []

	def add(self, cliente):
		self.lista.append(cliente)

	def procura(self, nome):
		for c in self.lista:
			if(c.nome == nome):
				return c
		return None

	def listagem(self):
		for c in self.lista:
			print(c.nome)
		

	def conta(self, numero):
		for c in self.lista:
			cto = c.procura(numero)
			if(cto is None):
				continue
			return cto
		return None
			

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
		print("Conta de " + self.cliente.nome)
		print("Extrato da conta numero: {0:10d}".format(self.numero))
		valor = 0
		for m in self.movimentacoes:
			valor = valor + m.valor
			print(m)
		print "{0:22s} {1:10.2f}".format("SALDO", valor)
		print "{0:22s} {1:10.2f}".format("DISPONIVEL", valor)
		print("*********************************")

		

	def deposito(self, valor):
		m = Movimentacao("D", valor)
		self.movimentacoes.append(m)

	def saque(self, valor):
		m = Movimentacao("S", valor)
		self.movimentacoes.append(m)

class ContaEspecial(Conta):
	def __init__(self, numero, limite, cliente):
		self.numero = numero
		self.limite = limite
		self.cliente = cliente
		self.movimentacoes = []

	def extrato(self):
		print("*********** EXTRATO *************")
		print("Conta de " + self.cliente.nome)
		print("Extrato da conta numero: {0:d}".format(self.numero))
		valor = 0
		for m in self.movimentacoes:
			valor = valor + m.valor
			print(m)
		print "{0:22s} {1:10.2f}".format("SALDO", valor)
		print "{0:22s} {1:10.2f}".format("LIMITE", self.limite)
		print "{0:22s} {1:10.2f}".format("DISPONIVEL", self.limite + valor)
		print("*********************************")


# Mostra o menu
def exibirMenu():
	clear()
	print("1 - Cadastro de Cliente")
	print("2 - Cadastro de Conta")
	print("3 - Deposito")
	print("4 - Saque")
	print("5 - Extrato")
	print("0 - Sair")
	option = int(input("Escolha uma opcao: "))
	return option

clientes = Clientes()

while True:
	op = exibirMenu()
	if (op == 0):
		print("Fim do Programa")
		break
	elif (op == 1):
		nome = raw_input("Nome do cliente: ")
		numero = input("Numero do cliente: ")
		cliente = Cliente(nome, numero)
		clientes.add(cliente)
	elif (op == 2):
		nome = raw_input("Nome do cliente: ")
		cliente = clientes.procura(nome)
		if(cliente is None):
			print("** CLIENTE NAO ENCONTRADO **")
			raw_input("Pressione <ENTER> para continuar")
			continue
			
		numero = input("Numero da conta: ")
		limite = float(input("Limite da conta: "))
		if (limite==0):
			cto = Conta(numero, cliente)
		else:
			cto = ContaEspecial(numero, limite, cliente)

		cliente.add(cto)

	elif (op == 3):
		conta = input("Numero da conta para deposito: ")
		cto = clientes.conta(conta)
		if(cto is None):
			print("** CONTA NAO ENCONTRADA **")
			raw_input("Pressione <ENTER> para continuar")
			continue
		
		cto.deposito(float(input("Valor do deposito: ")))
	elif (op == 4):
		conta = input("Numero da conta para saque: ")
		cto = clientes.conta(conta)
		if(cto is None):
			print("** CONTA NAO ENCONTRADA **")
			raw_input("Pressione <ENTER> para continuar")
			continue
		cto.saque(float(input("Valor do saque: ")))
	elif (op == 5):
		conta = input("Numero da conta para extrato: ")
		cto = clientes.conta(conta)
		if(cto is None):
			print("** CONTA NAO ENCONTRADA **")
			raw_input("Pressione <ENTER> para continuar")
			continue
		cto.extrato()
		raw_input("Pressione <ENTER> para continuar")
	elif (op==6):
		clientes.listagem()
		raw_input("Pressione <ENTER> para continuar")
	else:
		print("Opcao invalida")
		raw_input("Pressione <ENTER> para continuar")
	


