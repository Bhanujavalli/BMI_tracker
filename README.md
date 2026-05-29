# 🚀 Premium AI-Based BMI Health Tracker

Welcome to the **Premium AI Health Tracker**, a next-generation web platform built with Flask, SQLite, and modern frontend technologies. This application doesn't just calculate your BMI—it uses predictive mathematics, simulated generative AI coaching, and engaging gamification to help you stay motivated and hit your fitness goals!

## ✨ Key Premium Features

*   **🎙️ Voice-Activated Data Logging**  
    Built-in Javascript Web Speech API integration that allows you to click a button and log your weight completely hands-free by simply speaking the number into your microphone.
    
*   **📈 Predictive Health Forecasting**  
    Uses underlying Time-Series algorithm logic (Linear Regression) to calculate your past logged weights and plot a customized, forecasted dashed-trajectory line on your progress charts so you can see mathematically where your body is heading into the future.
    
*   **👤 Dynamic "Morphing" Avatar**  
    A highly responsive, custom-built SVG human silhouette that dynamically scales its width on your dashboard corresponding exactly to fluctuations in your recorded BMI.
    
*   **🤖 Generative AI Micro-Coaching**  
    An intelligent, context-aware recommendation engine that processes your metrics and pulls from randomized templates to simulate organic, conversational Generative LLM responses—providing you with a fresh daily personalized diet and lifestyle briefing.
    
*   **🔥 Gamified Health Streaks**  
    Tracks your logging consistency using a reliable backend persistence model, rewarding you with dynamic streak fire badges prominently displayed on the dashboard for consecutive logs.
    
*   **📷 Progress Photo Timelapse**  
    A secure file-uploading pipeline that saves your images and renders them in the Profile as a sleek visual sliding carousel for timeline body-transformation comparisons.
    
*   **🌟 Glassmorphism UI & Micro-Animations**  
    A cutting-edge aesthetic featuring translucent glass cards, sleek modern gradients, and smooth CSS keyframe micro-animations for an ultra-premium app feel.
    
*   **💯 Optimal Health Scoring System**  
    A composite algorithmic score (0-100) combining your consistency and distance from the optimal 22.0 median BMI, displayed natively on an animated SVG circular progress ring chart.

---

## 🛠️ Technology Stack
*   **Backend Layer:** Python 3, Flask, SQLAlchemy ORM (SQLite Database)
*   **Frontend Layer:** HTML5, CSS3, Bootstrap 5 (Grid System), Vanilla JS, Chart.js
*   **Security & Auth:** Flask-Login for secure session management and Werkzeug for password hashing.

---

## 🚀 How to Run Locally

1. **Open Your Terminal** inside the project folder.
2. **Activate the Virtual Environment**:
   ```bash
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # (Or .\venv\Scripts\activate.bat)
   ```
3. **Start the Flask Application**:
   ```bash
   python app.py
   ```
4. **View the App**: Open your web browser and navigate to `http://localhost:5000`

---

## 📁 Project Structure
- `app.py` - Application factory and database initializer.
- `models.py` - Defines SQLite models (Users, BMI Records, Progress Photos).
- `views.py` - Core routing, logic, and rendering engine.
- `utils/ai_recommender.py` - Generative logic template engine simulating AI output.
- `static/` - Glassmorphism CSS and UI elements.
- `templates/` - HTML structure with dynamic Jinja injection.
