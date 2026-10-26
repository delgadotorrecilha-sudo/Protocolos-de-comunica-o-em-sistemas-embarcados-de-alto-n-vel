from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

P_LED_VERDE = 20
P_LED_VERMELHO = 21

GPIO.setup(P_LED_VERDE, GPIO.OUT)
GPIO.setup(P_LED_VERMELHO, GPIO.OUT)

leitor = SimpleMFRC522()
USUARIO_AUTORIZADO = "15472530"


print("Aproxima a tag do leitor para leitura.")

try:
	while True:
		id, texto = leitor.read()
		texto = texto.strip()

		print(f"ID: {id}\n Texto : {texto}")

		if texto == USUARIO_AUTORIZADO:
			print("acesso liberado")
			GPIO.output(P_LED_VERDE, GPIO.HIGH)
			GPIO.output(P_LED_VERMELHO, GPIO.LOW)

		else:
			print("acesso negado")
			GPIO.output(P_LED_VERMELHO, GPIO.HIGH)
			GPIO.output(P_LED_VERDE, GPIO.LOW)

			sleep(3)

			GPIO.output(P_LED_VERDE, GPIO.LOW)
			GPIO.output(P_LED_VERMELHO, GPIO.LOW)

except KeyboardInterrupt:
	print("\nSistema encerrado.")
finally:
	GPIO.cleanup()
