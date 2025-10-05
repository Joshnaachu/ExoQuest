
# 🪐 ExoQuest - Exoplanet Detection Demo



## 🌌 Overview
ExoQuest is an interactive AI/ML-powered web demo that simulates how machine learning can detect exoplanets using telescope flux data.
Built with Streamlit, it provides a step-by-step workflow to load data, train a model, and test new inputs interactively.
## 🚀 Features
1. Load Sample Data

The app loads a dataset with flux readings from a telescope:

Flux_1, Flux_2, and Flux_3 represent light intensity variations.

Exoplanet (0 or 1) indicates whether a planet was detected based on flux changes.

Data visualization helps users understand the pattern behind exoplanet detection.

2. Train AI Model

A simple but powerful machine learning classifier is trained on the loaded data.

Displays model accuracy (as seen in the demo — 100% accuracy on the sample data).

Uses supervised learning to classify whether an exoplanet exists or not.

3. Try Your Own Input

Users can manually adjust Flux_1, Flux_2, and Flux_3 sliders.

The model instantly predicts:

✅ Exoplanet Detected

❌ No Exoplanet Detected

Interactive feedback allows users to experiment with telescope data intuitively.
## 🧠 Technologies Used

**Frontend & UI :**	 Streamlit

**Programming Language:**	Python

**ML Algorithm :**	Scikit-learn (classification model)
**Data Visualization :**	Pandas, Matplotlib/Seaborn (optional)
## ⚙️ How It Works
Load Data → Simulated telescope readings are loaded.

Train Model → AI model learns relationships between flux patterns and exoplanet presence.

Predict → User inputs new flux values to get instant predictions.
## 🧩 Example Data

| Flux_1 | Flux_2 | Flux_3 | Exoplanet |
|--------|--------|--------|------------|
| 0.8 | 0.2 | 0.7 | 1 |
| 0.5 | 0.1 | 0.3 | 0 |
| 0.9 | 0.6 | 0.4 | 0 |
| 0.3 | 0.8 | 0.95 | 1 |
| 0.3 | 0.4 | 0.2 | 0 |
## Deployment


```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/ExoQuest.git
cd ExoQuest

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the Streamlit app
streamlit run app.py
```

Then open your browser at **http://localhost:8501**.


## 🌠 Future Enhancements
Integration with real telescope datasets (e.g., Kepler or TESS missions).

Neural network-based model for complex pattern detection.

Interactive data visualization dashboards.

Exportable report summaries of predictions.
## 🧑‍💻 Author
**Developed by :** Joshna Maria Joseph

**Purpose :** To demonstrate how AI/ML techniques can identify exoplanets from telescope signal data.
