import telebot
import time
from gpiozero import MCP3008

# Настройки Wi-Fi и Telegram
ssid = "YourWiFiSSID"
password = "YourWiFiPassword"
bot_token = "YourTelegramBotToken"
chat_id = "YourTelegramChatID"

# Пины для компонентов
moisture_sensor_pin = 0  # Пин, к которому подключен датчик влажности почвы
pump_pin = 12  # Пин, к которому подключена помпа

# Пороговые значения для определения уровня влажности
dry_threshold = 0.7  # Пороговое значение для сухой почвы
wet_threshold = 0.3  # Пороговое значение для влажной почвы

# Время работы помпы в секундах
pump_duration = 5  # 5 секунд

# Настройка бота
bot = telebot.TeleBot(bot_token)

# Функция для отправки сообщения в Telegram
def send_telegram_message(message):
    bot.send_message(chat_id, message)

# Функция для подключения к Wi-Fi
def connect_to_wifi():
    print("Connecting to Wi-Fi...")
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "scan"])
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "add_network"])
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "set_network", "0", "ssid", f'"{ssid}"'])
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "set_network", "0", "psk", f'"{password}"'])
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "enable_network", "0"])
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "save_config"])
    wifi = subprocess.run(["/sbin/wpa_cli", "-i", "wlan0", "reconfigure"])
    print("Connected to Wi-Fi")

# Функция для чтения уровня влажности почвы
def read_moisture_level():
    adc = MCP3008(channel=moisture_sensor_pin)
    return adc.value

# Основной цикл программы
def main():
    while True:
        moisture_level = read_moisture_level()

        # Если почва слишком сухая, включаем помпу
        if moisture_level > dry_threshold:
            send_telegram_message("Сухая почва! Необходим полив.")
            # Включаем помпу на pump_duration секунд
            # Необходимо заменить на код, управляющий вашей помпой

        # Подождем некоторое время перед следующей проверкой
        time.sleep(60)

if __name__ == "__main__":
    main()
