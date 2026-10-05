import smbus
import time

ENDERECO_I2C = 0X08

bus = smbus.SMBus(1)

print("Controle do Led")
print("1 - Acende o LED")
print("0 - Apaga o LED")
print("Qualquer outro botão encerra o programa")

while True:
	try:
		comando_str = input("Introduza o comando:")
		comando = int(comando_str)

		if comando == 1:
			bus.write_byte(ENDERECO_I2C, 1)
			print("Comando 1 selecionado")
		elif comando == 0:
			bus.write_byte(ENDERECO_I2C, 0)
			print("Comando 0 selecionado")
		else:
			print("Encerrando o programa")
			break

	except ValueError:
		print("BURRO!!! Encerrando o programa")
		break
	except IOError:
		print("Erro de comunicação I2C. Verifique as ligações físicas")
		break

