# Student Performance Prediction System

## Project Overview
This project is a comprehensive machine learning-powered system designed to predict student academic outcomes based on multiple performance indicators. The system analyzes various factors like attendance, study hours, previous marks, and assignment scores to determine the likelihood of a student passing or failing their course.

## Personal Development Journey
This project represents my exploration into full-stack development with machine learning integration. I developed this system to understand how to combine modern web technologies with predictive analytics to create practical tools for educational institutions. The project demonstrates integration between frontend, backend, and machine learning components.

---

## 🚀 Tech Stack

### 🔧 Backend
- Node.js + Express
- MongoDB (Mongoose)
- JWT Authentication

### 🤖 ML Microservice
- Python 3.13
- Pandas, Scikit-learn, Joblib
- NumPy

### 💻 Frontend
- React.js (v19.1.0)
- Vite (v6.3.5)
- Material UI (v6.1.3)
- Tailwind CSS
- Recharts (for data visualization)
- React Router DOM, Formik + Yup, Toastify

---

## 📦 Features

- ✅ Teacher Registration & Authentication
- ✅ Student Data Management (Add, Update, Delete)
- ✅ AI-Powered Performance Prediction (Pass/Fail)
- ✅ Prediction History Tracking
- ✅ Interactive Data Visualization (Trend Charts)
- ✅ Responsive Web Interface
- ✅ Real-time Prediction Updates

---

## 🧮 Machine Learning Implementation

### Data Generation
- Custom synthetic data generator with realistic academic relationships
- 1000+ student records with correlations between factors
- Randomized outcomes based on weighted academic indicators

### Model Training
- Uses Random Forest algorithm for improved accuracy
- Features: Attendance (%), Study Hours per Day, Previous Marks (%), Assignment Score
- Performance: Typically 85-95% accuracy on synthetic data
- Model saved using joblib for efficient loading during predictions

### Prediction Process
- Node.js backend spawns Python process for ML inference
- Real-time prediction with immediate results
- Historical data stored for trend analysis

---

## 🛠️ Setup Instructions

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.8 or higher)
- MongoDB (running locally or cloud instance)

### Backend Setup
1. Navigate to server directory:
```bash
cd server
```

2. Install dependencies:
```bash
npm install
```

3. Install Python dependencies:
```bash
cd microservice
pip install -r requirements.txt
```

4. Create a `.env` file in the server directory:
```env
MONGO_URI="mongodb://localhost:27017/student-performance-predictor"
PORT=5000
JWT_SECRET="your-super-secret-jwt-key-change-in-production"
```

### Frontend Setup
1. Navigate to client directory:
```bash
cd client
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env` file in the client directory:
```env
VITE_APP_API_URL="http://localhost:5001/api"
```

### Running the Application
1. Generate training data:
```bash
cd server/microservice
python generate_training_data_1000.py
```

2. Train the ML model:
```bash
python train_model.py
```

3. Start the backend server:
```bash
cd ../..  # Go back to server directory
npm start
```

4. In a new terminal, start the frontend:
```bash
cd client
npm run dev
```

---

## 📁 Project Structure
<pre>
📦 root
├── 📁 server                           # Backend + ML Microservice
│   ├── 📁 microservice                 # Python ML code
│   │   ├── generate_training_data_1000.py
│   │   ├── predict.py
│   │   ├── student_performance_dataset.csv
│   │   ├── student_performance_model.joblib
│   │   ├── train_model.py
│   │   └── requirements.txt
│   ├── 📁 src                          # Node.js + Express backend
│   │   ├── 📁 controllers
│   │   ├── 📁 middlewares
│   │   ├── 📁 models
│   │   └── 📁 routes
│   ├── .env.example
│   ├── .gitignore
│   ├── package-lock.json
│   ├── package.json
│   └── server.js

├── 📁 client                          # React.js Frontend
│   ├── 📁 public
│   ├── 📁 src
│   │   ├── 📁 assets
│   │   ├── 📁 pages
│   │   │   ├── 📁 Auth
│   │   │   │   ├── LoginPage.jsx
│   │   │   │   └── RegisterPage.jsx
│   │   │   ├── AddStudentForm.jsx
│   │   │   ├── EditStudentForm.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Header.jsx
│   │   │   └── StudentDetails.jsx  # Enhanced with charts
│   │   ├── 📁 services
│   │   │   ├── api.js
│   │   │   └── toastNotifications.js
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── constants.js
│   │   ├── index.css
│   │   ├── main.jsx
│   │   └── routes.jsx
│   ├── .env
│   ├── .gitignore
│   ├── README.md
│   └── eslint.config.js

├── README.md

</pre>

---

## 📈 Data Visualization Features
The StudentDetails page includes:
- **Pass/Fail Prediction Trend Chart**: Shows the trend of pass/fail predictions over time
- **Academic Metrics Trend Chart**: Displays trends in attendance, study hours, previous marks, and assignment scores
- Interactive charts with tooltips and legend for better data interpretation

---

## 🤝 Contributing
This project represents my learning journey and contributions to make it better would be appreciated. Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

---

## 📝 Author
[Ansh Mahajan] - A passionate developer exploring the intersection of web development and machine learning.

---

## 🎯 Learning Outcomes
Through this project, I gained experience in:
- Full-stack web development with MERN stack
- Machine learning model integration with web applications
- Data visualization techniques
- Asynchronous processes between Node.js and Python
- Database design and management
- Authentication and security best practices

---

## 🔮 Future Enhancements
Potential improvements for the project include:
- More sophisticated ML algorithms (Neural Networks)
- Additional academic factors for prediction
- Email/SMS notifications for at-risk students
- Advanced analytics dashboard
- Mobile application development
- A/B testing for prediction model improvements

