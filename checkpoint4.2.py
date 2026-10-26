import smbus
import time

# Inicializa o barramento I2C 1 da Raspberry Pi
bus = smbus.SMBus(1)

# Mesmo endereço configurado no código do Arduino
DEVICE_ADDRESS = 0x08

print("Iniciando leitura I2C do potenciometro (Pressione Ctrl+C para encerrar)...")
print("-" * 60)

try:
    while True:
        try:
            # Solicita 2 bytes ao Arduino (registo virtual 0x00)
            dados = bus.read_i2c_block_data(DEVICE_ADDRESS, 0x00, 2)
            
            byte_alto = dados[0]
            byte_baixo = dados[1]
            
            # Reconstrução do valor de 10 bits (0 a 1023) usando bit shift
            valor_reconstruido = (byte_alto << 8) | byte_baixo
            
            # Calcula a tensão aproximada para visualização (referência de 5V)
            tensao = (valor_reconstruido * 5.0) / 1023.0
            
            print(f"Bytes recebidos: [MSB: {byte_alto:3d}, LSB: {byte_baixo:3d}] "
                  f"-> Valor 10-bits: {valor_reconstruido:4d} ({tensao:.2f} V)")
                  
        except OSError as e:
            print(f"Erro na comunicacao I2C (verifique cabos/level-shifter): {e}")
            
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nPrograma encerrado pelo utilizador.")