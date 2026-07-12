import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("m1.pkl")

st.title("🎓 Student Performance Prediction")

st.write("Enter the student's information.")

age = st.number_input("Age", 16, 70, 18)

father = st.slider("Father Education", -1, 6, 3)
mother = st.slider("Mother Education", -1, 6, 3)

income = st.slider("Family Income", 0, 16, 5)

phone = st.slider("Cell Phone Access", 0, 4, 2)
computer = st.slider("Computer Access", 0, 4, 1)

internet = st.selectbox("Internet Access", ["No", "Yes"])

if internet == "Yes":
    internet = 1
else:
    internet = 0

parents = father + mother

digital = phone + computer + internet

socio = income + parents

data = pd.DataFrame({
    "Age":[age],
    "Father_Education":[father],
    "Mother_Education":[mother],
    "Family_Income":[income],
    "Has_Cell_Phone":[phone],
    "Has_Computer":[computer],
    "Has_Internet_Yes":[internet],
    "Parents_Education":[parents],
    "Technology_Access":[digital],
    "Socioeconomic_Score":[socio]
})

prediction = model.predict(data)

labels = {
    0:"High",
    1:"Low",
    2:"Medium"
}

if st.button("Predict"):

    st.success(
        f"Predicted Performance : {labels[prediction[0]]}"
    )