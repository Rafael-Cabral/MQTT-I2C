import time
import dht
import machine
import json
from umqtt.simple import MQTTClient
from machine import I2C
from i2c_lcd import I2cLcd  # Certifique-se de ter a biblioteca i2c_lcd

# Função para conectar ao Wi-Fi
def connect_wifi(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Conectando ao Wi-Fi")
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass
    print("Conectado ao Wi-Fi")

# Configurações do LCD
LCD_ADDR = 0x27
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
LCD_SDA = 16
LCD_SCL = 17

# Configurações do Sensor DHT11
DHT_PIN = 2  

connect_wifi('SHARE-RESIDENTE', 'Share@residente23')

# Configurações MQTT
TOKEN = "BBUS-hlBUrkvVHJaxNyHAsZ4zVQbo8hqNrA"
DEVICE_LABEL = "Rasp"
VARIABLE_LABEL_1 = "temperature"
VARIABLE_LABEL_2 = "humidity"
VARIABLE_LABEL_3 = "position"

MQTT_BROKER = "industrial.api.ubidots.com"
MQTT_PORT = 1883
MQTT_TOPIC = "/v1.6/devices/{}".format(DEVICE_LABEL)

# Configuração e inicialização do LCD
i2c = I2C(0, sda=machine.Pin(LCD_SDA), scl=machine.Pin(LCD_SCL), freq=400000)
lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Inicializa o sensor DHT11
dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))

def build_payload(variable_1, variable_2):
    dht_sensor.measure()
    temp = dht_sensor.temperature()  
    hum = dht_sensor.humidity()      

    # Exibe a temperatura e umidade no LCD
    lcd.clear()
    lcd.putstr(f"Temp: {temp}C Hum: {hum}%")

    payload = {
        variable_1: temp,
        variable_2: hum,
    }
    return payload

def main():
    client = MQTTClient(DEVICE_LABEL, MQTT_BROKER, port=MQTT_PORT, user=TOKEN, password="")
    client.connect()

    payload = build_payload(VARIABLE_LABEL_1, VARIABLE_LABEL_2)

    print("[INFO] Tentando enviar dados")
    client.publish(MQTT_TOPIC, json.dumps(payload))
    print("[INFO] Dados enviados")
    client.disconnect()

if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)  

