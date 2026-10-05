#include <Wire.h> // inclui a biblioteca para usar a comunicação i2c

#define ENDERECO_I2C 0X08 // define o endereço desse arduino na rede i2c
const int pinoPotenciometro = A0; // avisa que o potenciômetro tá no pino analógico a0
int valorAnalogico = 0; // variável que vai guardar a leitura do potenciômetro

void setup(){
  Wire.begin(ENDERECO_I2C); // liga o i2c usando o endereço escolhido ali em cima
  Wire.onRequest(enviarDados); // quando o mestre pedir dados, avisa pra rodar a função 'enviardados'
  Serial.begin(9600); // liga o monitor serial pra gente ver o que tá rolando na tela
}

void loop(){
  valorAnalogico = analogRead(pinoPotenciometro); // faz a leitura do pino do potenciômetro e guarda na variável

  Serial.print("Valor lido no Arduino:"); // escreve a frase no monitor serial
  Serial.println(valorAnalogico); // mostra o número que foi lido e pula uma linha
  delay(500); // dá uma pausa de meio segundo pra não floodar a tela de informação
}

void enviarDados(){
  byte dados[2]; // cria uma caixinha pra guardar 2 bytes (já que o int é muito grande pra ir de uma vez só)

  dados[0] = highByte(valorAnalogico); // pega a metade de cima do valor e guarda no primeiro espaço
  dados[1] = lowByte(valorAnalogico); // pega a metade de baixo do valor e guarda no segundo espaço

  Wire.write(dados, 2); // manda os 2 bytes pelo i2c pra quem tiver pedindo
}
  dados[0] = highByte(valorAnalogico);
  dados[1] = lowByte(valorAnalogico);

  Wire.write(dados, 2);
}
