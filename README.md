# Weather Monitor - Hava Durumu Takip Uygulaması

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Flet Version](https://img.shields.io/badge/flet-0.7.0+-purple.svg)

[English](README_EN.md) | Türkçe

Modern ve kullanıcı dostu arayüzü ile OpenWeatherMap API kullanarak hava durumu takibi yapabileceğiniz bir masaüstü uygulaması.

![image](https://github.com/user-attachments/assets/9301448c-3f6f-4ab1-9479-5a5a55bed77c)


## ✨ Özellikler

- 🎨 Modern ve Material Design tabanlı kullanıcı arayüzü
- 🌡️ Gerçek zamanlı hava durumu takibi
- 🕒 Özelleştirilebilir güncelleme aralığı
- 📊 Sıcaklık, nem ve hava durumu bilgileri
- 📝 Detaylı işlem kayıtları
- 🌐 OpenWeatherMap API entegrasyonu
- 💫 Animasyonlu geçişler
- 🎯 Cross-platform uyumluluk

## 🔧 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- OpenWeatherMap API anahtarı

### Adımlar

1. Repo'yu klonlayın:
```bash
git clone https://github.com/your-username/weather-monitor.git
cd weather-monitor
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

3. OpenWeatherMap'ten API anahtarı alın:
   - [OpenWeatherMap](https://openweathermap.org/) sitesine üye olun
   - API anahtarınızı alın

## 💻 Kullanım

1. Uygulamayı başlatın:
```bash
python weather_app.py
```

2. API anahtarınızı girin
3. İstediğiniz şehri yazın
4. Güncelleme aralığını belirleyin
5. "Başlat" butonuna tıklayın

## 📦 Teknolojiler

- [Flet](https://flet.dev/) - Modern UI framework
- [Requests](https://docs.python-requests.org/) - HTTP kütüphanesi
- [OpenWeatherMap API](https://openweathermap.org/api) - Hava durumu verileri

## 📂 Proje Yapısı

```
weather-monitor/
├── weather_app.py
├── README.md
├── requirements.txt
├── LICENSE
└── screenshots/
    └── app_screenshot.png
```

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'feat: Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - ayrıntılar için [LICENSE](LICENSE) dosyasına bakınız.

## 📬 İletişim & Sosyal Medya

- GitHub: [github.com/onder7](https://github.com/onder7)
- LinkedIn: [Mustafa Önder Aköz](https://www.linkedin.com/in/mustafa-önder-aköz-23174592)
- Medium: [@onder7](https://medium.com/@onder7)
- Web: [ondernet.net](https://ondernet.net)

## 📋 Requirements.txt İçeriği

```
flet>=0.7.0
requests>=2.28.0
```

---

© 2024 Mustafa Önder Aköz - Tüm hakları saklıdır.

---

## 🔜 Gelecek Özellikler

- [ ] Çoklu şehir desteği
- [ ] Koyu tema / Açık tema seçeneği
- [ ] Farklı dil desteği
- [ ] Hava durumu bildirimleri
- [ ] 5 günlük hava durumu tahmini
- [ ] Hava kalitesi bilgileri
- [ ] Grafiksel veriler
- [ ] Favori şehirler listesi

## 💡 Bilinen Sorunlar

- API istek limiti aşıldığında uygulamanın davranışı
- Bazı şehir isimleri için encoding sorunları

Herhangi bir sorun veya öneriniz için [Issues](https://github.com/onder7/weather-monitor/issues) sayfasını kullanabilirsiniz.
