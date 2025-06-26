import streamlit as st
import matplotlib.pyplot as plt

# Titre et description
st.title("💡 Simulateur d'émissions CO₂ évitées")
st.markdown("""
Ce simulateur permet d’estimer les émissions de CO₂ évitées grâce à un système de **télégestion de l’éclairage public**.
""")

# Entrées utilisateur
st.sidebar.header("Paramètres du scénario")
nb_lampadaires = st.sidebar.number_input("Nombre de lampadaires", min_value=1, value=100)
puissance = st.sidebar.number_input("Puissance unitaire (W)", min_value=1, value=100)
heures_an = st.sidebar.number_input("Heures d'éclairage/an", min_value=1, value=4000)
facteur_emission = st.sidebar.number_input("Facteur d'émission (kgCO₂/kWh)", min_value=0.0, value=0.056)
taux_economie = st.sidebar.slider("Taux d'économie (%)", min_value=0, max_value=100, value=40)

# Calculs
conso_kwh = nb_lampadaires * puissance * heures_an / 1000  # en kWh
emissions_base = conso_kwh * facteur_emission
emissions_reduites = emissions_base * (1 - taux_economie / 100)
emissions_evitees = emissions_base - emissions_reduites

# Résultats
st.subheader("📊 Résultats")
st.metric("Consommation annuelle (kWh)", f"{conso_kwh:.0f}")
st.metric("Émissions sans télégestion (kgCO₂)", f"{emissions_base:.2f}")
st.metric("Émissions avec télégestion (kgCO₂)", f"{emissions_reduites:.2f}")
st.metric("🎯 GES évitées (kgCO₂)", f"{emissions_evitees:.2f}")

# Graphique
fig, ax = plt.subplots()
ax.bar(["Sans télégestion", "Avec télégestion"], [emissions_base, emissions_reduites], color=["red", "green"])
ax.set_ylabel("kgCO₂/an")
st.pyplot(fig)
