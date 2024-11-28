import flet as ft
import requests
import logging
from datetime import datetime
import time

class WeatherConfig:
    def __init__(self, city, api_key, units='metric'):
        self.city = city
        self.api_key = api_key
        self.units = units

class WeatherApp:
    def __init__(self):
        self.monitoring = False
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='weather_app.log'
        )

    def main(self, page: ft.Page):
        # Sayfa ayarları
        page.title = "Hava Durumu Takip"
        page.window_width = 600
        page.window_height = 800
        page.padding = 20
        page.theme_mode = ft.ThemeMode.LIGHT
        page.vertical_alignment = ft.MainAxisAlignment.START

        # API Key girişi
        self.api_key_field = ft.TextField(
            label="API Key",
            width=400,
            text_style=ft.TextStyle(size=14),
        )

        # Şehir girişi
        self.city_field = ft.TextField(
            label="Şehir",
            width=400,
            value="Istanbul",
            text_style=ft.TextStyle(size=14),
        )

        # Güncelleme aralığı
        self.interval_field = ft.TextField(
            label="Güncelleme Aralığı (dakika)",
            width=200,
            value="60",
            text_style=ft.TextStyle(size=14),
        )

        # Başlat/Durdur butonları
        self.start_button = ft.ElevatedButton(
            text="Başlat",
            on_click=self.start_monitoring,
            width=150,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN_600,
        )

        self.stop_button = ft.ElevatedButton(
            text="Durdur",
            on_click=self.stop_monitoring,
            width=150,
            disabled=True,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.RED_600,
        )

        # Log alanı
        self.log_view = ft.TextField(
            multiline=True,
            read_only=True,
            min_lines=15,
            max_lines=15,
            width=550,
            text_size=14,
        )

        # Hava durumu kartı
        self.weather_card = ft.Card(
            visible=False,
            width=550,
            content=ft.Container(
                padding=20,
                content=ft.Column(
                    controls=[
                        ft.Text("Hava Durumu Bilgileri", size=20, weight=ft.FontWeight.BOLD),
                        ft.Divider(),
                        ft.Text("", size=16, weight=ft.FontWeight.W_500),  # Şehir
                        ft.Text("", size=16),  # Sıcaklık
                        ft.Text("", size=16),  # Nem
                        ft.Text("", size=16),  # Durum
                    ],
                )
            )
        )

        # Sayfa düzeni
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Hava Durumu Takip", size=24, weight=ft.FontWeight.BOLD),
                    self.api_key_field,
                    self.city_field,
                    self.interval_field,
                    ft.Row(
                        controls=[self.start_button, self.stop_button],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    self.weather_card,
                    ft.Text("İşlem Kayıtları", size=16, weight=ft.FontWeight.BOLD),
                    self.log_view,
                ],
                spacing=20,
            )
        )

    def get_weather(self, config):
        try:
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': config.city,
                'appid': config.api_key,
                'units': config.units
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.log(f"API isteği başarısız: {e}", "error")
            return None
        except Exception as e:
            self.log(f"Beklenmeyen hata: {e}", "error")
            return None

    def log(self, message, level="info"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        
        # GUI log alanını güncelle
        current_logs = self.log_view.value if self.log_view.value else ""
        self.log_view.value = current_logs + log_message
        self.log_view.update()

        # Dosyaya kaydet
        if level == "error":
            logging.error(message)
        else:
            logging.info(message)

    def update_weather_card(self, weather_data):
        if not weather_data:
            return

        try:
            weather = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            city = weather_data['name']

            # Kart içeriğini güncelle
            card_content = self.weather_card.content.content.controls
            card_content[2].value = f"Şehir: {city}"
            card_content[3].value = f"Sıcaklık: {temp}°C"
            card_content[4].value = f"Nem: {humidity}%"
            card_content[5].value = f"Durum: {weather}"
            
            self.weather_card.visible = True
            self.weather_card.update()
        except Exception as e:
            self.log(f"Hava durumu kartı güncellenirken hata: {e}", "error")

    def start_monitoring(self, e):
        if not self.api_key_field.value:
            self.log("API Key girilmesi zorunludur!", "error")
            return

        try:
            interval = int(self.interval_field.value)
            if interval <= 0:
                raise ValueError("Geçersiz aralık")
        except ValueError:
            self.log("Geçerli bir güncelleme aralığı giriniz!", "error")
            return

        self.monitoring = True
        self.start_button.disabled = True
        self.stop_button.disabled = False
        self.start_button.update()
        self.stop_button.update()
        
        self.log("Hava durumu takibi başlatıldı.")
        self.check_weather(e.page)

    def stop_monitoring(self, e):
        self.monitoring = False
        self.start_button.disabled = False
        self.stop_button.disabled = True
        self.start_button.update()
        self.stop_button.update()
        self.log("Hava durumu takibi durduruldu.")

    def check_weather(self, page):
        if not self.monitoring:
            return

        config = WeatherConfig(
            city=self.city_field.value,
            api_key=self.api_key_field.value
        )

        weather_data = self.get_weather(config)
        if weather_data:
            self.update_weather_card(weather_data)
            self.log(f"Hava durumu güncellendi - {config.city}")

        if self.monitoring:
            interval = int(self.interval_field.value) * 60 * 1000  # milisaniyeye çevir
            page.after(interval, lambda _: self.check_weather(page))

def main():
    app = WeatherApp()
    ft.app(target=app.main)

if __name__ == "__main__":
    main()
