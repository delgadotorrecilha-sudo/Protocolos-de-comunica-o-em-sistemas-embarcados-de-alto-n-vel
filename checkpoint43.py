import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
leitor = SimpleMFRC522()

texto = "15472530"

print("aproxima a tag do leitor para gravar.")
leitor.write(texto)
print("Concluido")
