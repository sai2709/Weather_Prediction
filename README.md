# ☁️ Weather Forecast Web App

A simple and elegant **Flask-based web application** that displays current weather information for any city using the **OpenWeatherMap API**.

---

## 🚀 Features

- 🌤️ Real-time weather updates
- 🔍 Search by city name
- 🌡️ Displays:
  - Current temperature
  - Feels like temperature
  - Humidity
  - Weather description and icon
- ✅ Error handling for invalid input, city not found, and network/API errors

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **API**: [OpenWeatherMap API](https://openweathermap.org/api)
- **Frontend**: HTML, Jinja2 (Bootstrap optional for styling)

---

## ⚙️ Setup Instructions

### 📁 Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```
🐍 Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate
```
📦 Install Dependencies
```
pip install -r requirements.txt

```
🔑 Set Up Your API Key
Go to OpenWeatherMap and sign up to get your free API key.

In app.py, replace:
```
API_KEY = "Enter your API"
API_KEY = "your_actual_api_key_here"

```
🏃 Run the App
```
python app.py
```
🧾 File Structure
```
weather-app/
├── templates/
│   └── index.html
├── static/               # (Optional) CSS/images/icons
├── app.py
├── requirements.txt
└── README.md
```



