# 💎 Elmas Fiyat Tahmini

Elmas özelliklerini girerek tahmini piyasa fiyatını öğrenebileceğiniz yapay zeka destekli web uygulaması.

🔗 **Canlı Demo:** https://diomands-predictor.onrender.com

---

## 🚀 Proje Hakkında

Bu proje, 54.000 elmas kaydından oluşan bir veri seti kullanılarak eğitilmiş bir makine öğrenmesi modelini içermektedir. Kullanıcı elmasın özelliklerini girer, model tahmini fiyatı döndürür.

---

## 📊 Model Performansı

| Metrik | Sonuç |
|--------|-------|
| R² | 0.98 |
| MAE | $277 |
| RMSE | $534 |
| Algoritma | Gradient Boosting |
| Eğitim verisi | 43.152 satır |
| Test verisi | 10.788 satır |

---

## 🛠️ Kullanılan Teknolojiler

- **Python** — model eğitimi ve backend
- **Scikit-learn** — Gradient Boosting algoritması
- **Flask** — web sunucusu
- **SQLite** — tahmin geçmişi veritabanı
- **HTML/CSS/JavaScript** — kullanıcı arayüzü
- **Render** — deployment

---

## 📁 Proje Yapısı
```
diamonds_predictor/
├── data/
│   └── diamonds.csv      # Veri seti (54K satır)
├── templates/
│   ├── index.html        # Ana sayfa
│   └── gecmis.html       # Geçmiş tahminler
├── app_flask.py          # Flask backend
├── notebook.ipynb        # Model eğitim notebook'u
├── model.pkl             # Eğitilmiş model
└── requirements.txt      # Bağımlılıklar
```
## ⚙️ Kurulum

```bash
git clone https://github.com/senapoyraz/diomands_predictor.git
cd diomands_predictor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app_flask.py
```

---

## 📌 Özellikler
```
- Elmas özelliklerine göre fiyat tahmini
- Geçmiş tahminlerin veritabanına kaydedilmesi
- Responsive ve modern arayüz
```