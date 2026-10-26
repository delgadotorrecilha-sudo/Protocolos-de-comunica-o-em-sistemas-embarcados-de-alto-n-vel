// Luís Carlos Delgado Torrecilha - 15472530
// Beatriz Fonseca Silva - 15653959
#include <Wire.h> // Importa a biblioteca Wire, que é a biblioteca padrão do Arduino para comunicação I2C

#define ENDERECO_I2C 0X08 // Define uma constante para o endereço I2C deste Arduino (configurado como dispositivo escravo no endereço 8)

const int pinoPotenciometro = A0; // Define que o potenciômetro está conectado ao pino analógico A0 da placa
int valorAnalogico = 0; // Cria uma variável inteira global para armazenar o valor lido do potenciômetro, iniciando em 0

// A função setup() é executada apenas uma vez quando o Arduino é ligado ou resetado
void setup(){
  // Inicializa o barramento I2C atribuindo a este Arduino o endereço definido acima (0x08), configurando-o como escravo
  Wire.begin(ENDERECO_I2C);
  
  // Configura um "gatilho" (interrupção): sempre que o dispositivo mestre solicitar informações, a função 'enviarDados' será executada automaticamente
  Wire.onRequest(enviarDados);
  
  // Inicializa a comunicação serial a uma taxa de 9600 bits por segundo para permitir a visualização dos dados no Monitor Serial do computador
  Serial.begin(9600);
}

// A função loop() é o corpo principal do programa e se repete infinitamente
void loop(){
  // Lê o sinal analógico atual do potenciômetro no pino A0. O Arduino converte a tensão (0 a 5V) em um número de 10 bits (0 a 1023)
  valorAnalogico = analogRead(pinoPotenciometro);

  // Imprime o texto descritivo no Monitor Serial do computador
  Serial.print("Valor lido no Arduino:");
  
  // Imprime o valor numérico lido na mesma linha e pula para a próxima linha (println)
  Serial.println(valorAnalogico);
  
  // Pausa a execução por 500 milissegundos (meio segundo) para não sobrecarregar a porta serial com impressões muito rápidas
  delay(500);
}

// Esta é a função de serviço (handler) associada ao evento Wire.onRequest configurado no setup()
void enviarDados(){
  // Cria um array (vetor) de 2 posições do tipo byte. 
  // Isso é necessário porque o protocolo I2C transmite dados em pacotes de 8 bits (1 byte), e o valor analógico (até 1023) ocupa 16 bits (2 bytes).
  byte dados[2];

  // A função highByte() extrai a metade superior (os 8 bits mais significativos) da variável inteira e armazena na posição 0 do vetor
  dados[0] = highByte(valorAnalogico);
  
  // A função lowByte() extrai a metade inferior (os 8 bits menos significativos) da variável inteira e armazena na posição 1 do vetor
  dados[1] = lowByte(valorAnalogico);

  // Envia o array contendo os 2 bytes fragmentados de volta para o dispositivo mestre através do barramento I2C
  Wire.write(dados, 2);
}