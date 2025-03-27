# Web Performance Monitoring with Spark

## 📌 Objective
This project allows you to **monitor the performance** of a website in real time from logs.

## 📂 Project structure
- `app/main.py` → Log analysis with Spark Streaming.
- `scripts/generate_logs.py` → Generate logs for testing.
- `scripts/config.py` → Project configuration.
- `data/access.log` → Analyzed log file.
- `docs/` → Project documentation.

## 🚀 Installation
1. **Run project**  
   ```bash
   git clone https://github.com/ton-repo/projet_spark_web.git
   cd projet_spark_web 
   ```

2. **Installing dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Start log simulation** 
   ```bash
   python scripts/generate_logs.py
   ```
4. **Run Spark analysis** 
   ```bash
   python app/main.py
   ```

## 🛠 Features
Analyzes site requests and errors.

Calculates average response time.

Detection of 500 and 404 errors.


