# 🐍 Simple API Python Projects

A collection of simple Python programs that use different APIs to practice working with HTTP requests, JSON, and automation.

---

## Project List

### 1. **request-tutorial/**
Basic examples of making API calls with the `requests` library.  
- GET requests.  
- Parsing JSON responses.  
- Error handling with `raise_for_status()`.

---

### 2. **kanye-quotes/**
A fun program that fetches random **Kanye West quotes** from the [Kanye REST API](https://kanye.rest/) and displays them.  
- Includes simple GUI with Tkinter.  
- Assets: `background.png`, `kanye.png`.

---

### 3. **api-parameter/**
Fetches **sunrise and sunset times** using the [Sunrise-Sunset API](https://sunrise-sunset.org/api) with parameters (latitude & longitude).  
- Converts UTC to local time.  
- Demonstrates handling API query parameters.  

---

### 4. **issoverhead/**
Check if the **International Space Station (ISS)** is above your location at night and send an email alert.  
- Uses [Open Notify ISS API](http://api.open-notify.org/iss-now.json)  
- Uses [Sunrise-Sunset API](https://sunrise-sunset.org/api)  
- Sends email via Gmail SMTP.

---

### 5. **quizzler-app/**
A **quiz game** that fetches trivia questions from the [Open Trivia Database API](https://opentdb.com/).  
- Built with **Tkinter GUI**.  
- Displays True/False questions with interactive buttons.  
- Tracks and displays score in real-time.  
- Includes a **restart feature** when the quiz ends.  

**Project structure:**
- `question_model.py` → Question class  
- `data.py` → Fetches quiz data from API  
- `quiz_brain.py` → Handles quiz logic  
- `ui.py` → Tkinter interface  
- `main.py` → Entry point  

---

## Setup & Run

### 1. Clone this repo:
```
git clone https://github.com/Fxf28/simple-api-python.git
cd simple-api-python
```

---

### 2. Create a virtual environment (optional but recommended):
```
# With venv
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# With conda
conda create --name myenv
conda activate myenv
```

---

### 3. Install dependencies
```
pip install -r requirements.txt
# or
conda install --yes --file requirements.txt
```

---

### 4. Run a project
```
# Example: run the ISS Overhead Notifier
cd issoverhead
python main.py
```
```
# Example: run the Kanye Quotes GUI
cd kanye-quotes
python main.py
```
```
# Example: run the Quizzler App
cd quizzler-app
python main.py
```

---

### Special Setup Notes
For issoverhead/, create a config.py file inside the folder with your details:
```
MY_LAT = 51.5074      # Your latitude
MY_LNG = -0.1278      # Your longitude
EMAIL = "your_email@example.com"
PASSWORD = "your_app_password"
```

> Make sure config.py is in .gitignore so you don’t expose your credentials.
