import smbus # importa a biblioteca pra conseguir usar a comunicação i2c na raspberry
import time # importa a biblioteca de tempo (apesar de não estar sendo usada aqui)

ENDERECO_I2C = 0X08 # define o mesmo endereço do arduino pra eles conseguirem se achar

bus = smbus.SMBus(1) # avisa que vamos usar o barramento i2c número 1 (o padrão da maioria das placas)

# imprime um menuzinho na tela pra explicar como a coisa funciona
print("Controle do Led")
print("1 - Acende o LED")
print("0 - Apaga o LED")
print("Qualquer outro botão encerra o programa")

while True: # cria um loop infinito pra ficar perguntando o tempo todo
	try: # tenta rodar o bloco de código abaixo. se der zika, ele pula pros 'except'
		comando_str = input("Introduza o comando:") # pede pro usuário digitar algo e guarda como texto
		comando = int(comando_str) # converte o texto que o usuário digitou pra um número inteiro

		if comando == 1: # se o cara digitou 1
			bus.write_byte(ENDERECO_I2C, 1) # manda o byte 1 lá pro arduino pelo i2c
			print("Comando 1 selecionado") # avisa na tela o que foi feito
		elif comando == 0: # mas se o cara digitou 0
			bus.write_byte(ENDERECO_I2C, 0) # manda o byte 0 pro arduino
			print("Comando 0 selecionado") # avisa na tela também
		else: # se o cara digitou qualquer outro número (2, 5, 99...)
			print("Encerrando o programa")
			break # quebra o loop infinito e o programa acaba

	except ValueError: # se o usuário digitar uma letra ou palavra em vez de número, cai aqui
		print("Encerrando o programa")
		break # quebra o loop
	except IOError: # se der algum problema físico (fio solto, arduino sem energia)
		print("Erro de comunicação I2C. Verifique as ligações físicas") # avisa pra checar os cabos
		break # também quebra o loop
