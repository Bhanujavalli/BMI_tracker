# AI-Based BMI Health Tracker System

A complete full-stack web application designed to track user BMI data and provide intelligent, rule-based AI recommendations for health risks, diets, and exercise. It features a dashboard aesthetic with customized dark mode styling and glassmorphism UI elements.

## Features Included
1. **User Authentication:** Secure login and registration using modern hashing (`scrypt`).
2. **Smart AI Health Recommendations:** Generates specific dietary strategies, fitness regiments, and health risk profiles directly dependent on user age, gender, and live BMI categorizations. 
3. **Strict Validation:** Prevents erratic/impossible changes to fundamental body metrics (e.g. height cannot jump unrealistically post-registration) preventing bad data.
4. **Progress Analytics:** Visualizes historical weight and BMI trends using an interactive interactive `Chart.js` curve.
5. **Comprehensive Reports:** Generates a printable, summary-style view of all tracking sessions suitable for a physician.

## Technology Stack
- **Frontend:** HTML5, CSS3, Bootstrap 5, FontAwesome, Chart.js
- **Backend:** Python + Flask framework
- **Database:** SQLAlchemy ORM (Defaults to zero config `SQLite` for easy local testing, but includes `database.sql` script for full MySQL database integration as requested).

---

## Setup Instructions
1. **Navigate to the Project Directory:** Ensure you are in the application root where `app.py` resides.
2. **Setup Virtual Environment:** (Recommended)
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Database Setup (SQLite vs MySQL):**
   - **SQLite (Default & Ready-To-Run):** Simply running the application creates a `bmi_tracker.db` automatically in the root folder. You do not need to install any database servers.
   - **MySQL (As requested in design requirements):** If you prefer to deploy using MySQL:
     1. Import `database.sql` into your MySQL server to build the schema.
     2. Open `config.py` and modify `SQLALCHEMY_DATABASE_URI` to equal `'mysql+pymysql://username:password@localhost/bmi_db'`.

---

## How to Run Locally
1. Ensure your virtual environment is active.
2. Execute the Flask runner:
   ```bash
   python app.py
   ```
3. Open a browser and navigate to `http://127.0.0.1:5000`
4. Register a new user, log your initial BMI data, and explore the AI-generated health results!

## Project Structure Overview
- `app.py` - Application factory and DB initializer.
- `models.py` - User and History tables definition.
- `config.py` - Core configuration settings.
- `auth.py` - Login, logout, and registration logic.
- `views.py` - Core application routing and dashboard data collation.
- **`utils/`**
  - `ai_recommender.py` - Core BMI formula classification & AI generation matrix.
  - `validators.py` - Logic securing database consistency against erratic human inputs.
- **`static/`** - Home to custom CSS styling.
- **`templates/`** - Frontend UI definitions rendered via Jinja2 engine.

**Enjoy presenting this AI-Based Health Tracking software for your project demo!**
