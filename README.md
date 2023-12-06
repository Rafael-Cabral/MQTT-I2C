# Medidor de Temperatura com Comunicação Serial I2C

O projeto do Medidor de Temperatura com Display LED I2C é uma solução eficiente para monitoramento de temperatura em tempo real. Este projeto foi desenvolvido utilizando o microcontrolador Raspberry Pi Pico, conhecido pela sua versatilidade, juntamente com um sensor de temperatura e um display LED I2C para uma visualização clara e direta.

O objetivo deste projeto é fornecer um dispositivo confiável e fácil de usar para medir temperaturas em diferentes ambientes, como em casa, escritórios, carros ou até mesmo saídas de ar de nossos computadores, como foi visto nos vídeos anteriores. Através de uma interface simplificada, o usuário pode obter leituras de temperatura precisas e instantâneas, exibidas de maneira clara no display LED I2C.

Este documento README destina-se a fornecer todas as informações necessárias para compreender, montar e operar o Medidor de Temperatura com Display LED I2C. Aqui você encontrará detalhes sobre o hardware utilizado, a descrição do funcionamento da comunicação I2C e serial, além de um vídeo demonstrativo que ilustra o funcionamento prático do projeto.

## Conteúdo
- [Descrição do Hardware](#descrição-do-hardware)
- [Comunicação I2C e Serial](#comunicação-i2c-e-serial)
- [Vídeo Demonstrativo](#vídeo-demonstrativo)
- [Como Usar](#como-usar)
- [Licença](#licença)

## Descrição do Hardware

No projeto de Medidor de Temperatura e Umidade, utilizamos componentes-chave para criar um dispositivo eficiente e confiável. A seguir estão os detalhes dos componentes utilizados:

1. **Raspberry Pi Pico W**: O cérebro do nosso projeto, o Raspberry Pi Pico W é um microcontrolador de baixo custo, mas poderoso, com capacidades de Wi-Fi integradas. Ele oferece excelente desempenho para processar os dados de temperatura e umidade, além de facilitar a comunicação com outros dispositivos ou redes.

2. **Sensor de Temperatura e Umidade DHT11**: Este sensor é utilizado para medir a temperatura e a umidade do ambiente. O DHT11 é conhecido por sua facilidade de uso e precisão razoável, tornando-o ideal para aplicações domésticas e educacionais.

3. **Display LCD I2C 16x2**: O display LCD I2C 16x2 é usado para mostrar as leituras de temperatura e umidade. Sua interface I2C simplifica a conexão com o Raspberry Pi Pico W, reduzindo a quantidade de pinos necessários para a comunicação e permitindo uma montagem mais organizada e menos complexa.

### Diagrama de Blocos

O diagrama de blocos detalhado abaixo, ajuda a ilustrar a conexão entre o Raspberry Pi Pico W, o sensor DHT11 e o display LCD I2C 16x2. O diagrama inclui:

- As conexões de alimentação (VCC, GND) e de dados (SCL, SDA para o LCD I2C; pinos de sinal para o DHT11) entre o Raspberry Pi Pico W e os outros componentes.
- Uma representação clara de como cada componente está conectado ao microcontrolador.
- Detalhes relevantes para cada componente, como pinagem e funções.

![]()

## Comunicação I2C e Serial

### Comunicação I2C

Explicação de como o Raspberry Pi Pico se comunica com o sensor I2C, incluindo detalhes técnicos sobre o protocolo I2C.

### Comunicação Serial

Descrição da comunicação serial entre o Raspberry Pi Pico e o PC, incluindo a configuração necessária e como os dados são transmitidos.

## Vídeo Demonstrativo

O vídeo demonstrativo pode ser acessado através [desse link, clicando aqui](https://youtu.be/aSM7Uxoy3-Q).

Como complemento, abaixo estão os links dos vídeos anteriores da nossa solução:

[MQTT + Medidor de temperatura (2ª ponderada)]()
[Medidor de temperatura + Front (1ª ponderada]()

## Como Usar

Instruções passo a passo sobre como configurar e usar o sistema.

## Licença

Informações sobre a licença do projeto.
