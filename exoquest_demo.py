import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.title("🔭 ExoQuest - Exoplanet Detection Demo")

st.markdown("""
Welcome to **ExoQuest**!  
This demo shows how AI/ML can help detect **exoplanets** from telescope data. 🚀
""")

st.subheader("Step 1: Load Sample Data")
data = {
    "Flux_1": [0.8, 0.2, 0.5, 0.9, 0.3],
    "Flux_2": [0.7, 0.1, 0.6, 0.8, 0.4],
    "Flux_3": [0.9, 0.3, 0.4, 0.95, 0.2],
    "Exoplanet": [1, 0, 1, 1, 0]
}
df = pd.DataFrame(data)                      
st.dataframe(df)

st.subheader("Step 2: Train AI Model")
X = df.drop("Exoplanet", axis=1)
y = df["Exoplanet"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
st.success(f"✅ Model trained with accuracy: {acc*100:.2f}%")

st.subheader("Step 3: Try Your Own Input")
flux1 = st.slider("Flux_1", 0.0, 1.0, 0.5)
flux2 = st.slider("Flux_2", 0.0, 1.0, 0.5)
flux3 = st.slider("Flux_3", 0.0, 1.0, 0.5)

user_input = pd.DataFrame([[flux1, flux2, flux3]], columns=["Flux_1", "Flux_2", "Flux_3"])
prediction = model.predict(user_input)[0]

if prediction == 1:
    st.success("🌍 Exoplanet Detected!")
else:
    st.error("❌ No Exoplanet Detected.")
