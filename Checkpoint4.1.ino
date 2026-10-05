#include <Wire.h>

#define ENDERECO_I2C 0X08
const int pinoPotenciometro = A0;
int valorAnalogico = 0;

void setup(){
  Wire.begin(ENDERECO_I2C);
  Wire.onRequest(enviarDados);
  Serial.begin(9600);
}

void loop(){
  valorAnalogico = analogRead(pinoPotenciometro);

  Serial.print("Valor lido no Arduino:");
  Serial.println(valorAnalogico);
  delay(500);
}

void enviarDados(){
  byte dados[2];

  dados[0] = highByte(valorAnalogico);
  dados[1] = lowByte(valorAnalogico);

  Wire.write(dados, 2);
}