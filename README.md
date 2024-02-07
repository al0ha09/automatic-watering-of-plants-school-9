# automatic-watering-of-plants-school-9
# Smart Irrigation System with Telegram Notification (Arduino Uno)

This Arduino sketch enables an automated smart irrigation system using an Arduino Uno, a soil moisture sensor, and a water pump. The system periodically measures the soil moisture level and sends a notification via Telegram if the soil is too dry, indicating the need for watering. Additionally, it activates the water pump to irrigate the soil for a specified duration.

## Prerequisites

- Arduino Uno
- Soil moisture sensor
- Water pump
- Telegram bot token
- Telegram chat ID
- Wi-Fi shield or module (if using Wi-Fi for internet connectivity)

## Installation

1. Connect the soil moisture sensor to the Arduino analog pin specified in the `moisture_sensor_pin` variable.
2. Connect the water pump to the digital pin specified in the `pump_pin` variable.
3. Install the necessary libraries:

   - [Arduino Telegram Bot Library](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot)
   - (If using Wi-Fi) Libraries for your Wi-Fi shield/module (e.g., ESP8266WiFi.h)

## Configuration

- Update the following variables in the sketch with your Wi-Fi network credentials and Telegram bot token/chat ID:

    ```cpp
    const char* ssid = "YourWiFiSSID";
    const char* password = "YourWiFiPassword";
    const char* botToken = "YourTelegramBotToken";
    const int chatId = YourTelegramChatID;
    ```

- Adjust the threshold values and pump duration as per your requirements:

    ```cpp
    const float dryThreshold = 0.7; // Threshold value for dry soil
    const float wetThreshold = 0.3; // Threshold value for wet soil
    const unsigned long pumpDuration = 5000; // Pump activation duration in milliseconds
    ```

## Usage

1. Upload the sketch to your Arduino Uno board.
2. The sketch will connect to Wi-Fi (if applicable), monitor the soil moisture level, and send Telegram notifications if the soil is too dry.
3. Ensure your Telegram bot is added to the desired chat and has permission to send messages.

## Customization

- You can extend the functionality by integrating additional sensors (e.g., temperature, humidity) or adding more complex logic for irrigation scheduling.
- Implement error handling and logging to enhance robustness and debug potential issues.
- Consider using a real-time clock (RTC) module for accurate timing if precise scheduling is required.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
