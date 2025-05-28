import streamlit as st
import matplotlib.pyplot as plt

st.title("Uw CO2-voetafdruk brekenen")

# Invoervelden
auto = st.number_input("Hoeveel km reis jij per jaar met uw auto?", min_value=0, step=1)
trein = st.number_input("Hoeveel km reis jij per jaar met de trein?", min_value=0, value=0, step=1)
vliegtuig = st.number_input("Hoeveel km reis jij per jaar met het vliegtuig?", min_value=0, value=0, step=1)
elektriciteit = st.number_input("Hoeveel elektriciteit in kWh verbruikt u per maand?", min_value=0, value=0, step=1)
vlees = st.number_input("Hoeveel kilogram vlees consumeert u per jaar?", min_value=0, value=0, step=1)

if st.button("Bereken CO2-uitstoot"):
    uitstootAuto = 0.2 * auto
    uitstootTrein = 0.05 * trein
    uitstootVliegtuig = 0.25 * vliegtuig
    verbruikElektriciteit = 0.45 * 12 * elektriciteit
    consumptieVlees = 27 * vlees
    totaal = uitstootAuto + uitstootTrein + uitstootVliegtuig + verbruikElektriciteit + consumptieVlees
    
    st.write(f"##### Uw totale CO2-uitstoot per jaar: **{int(totaal)} kg**")
    st.write(f"- 🚗 Auto: **{int(uitstootAuto)} kg**")
    st.write(f"- 🚆 Trein: **{int(uitstootTrein)} kg**")
    st.write(f"- ✈️ Vliegtuig: **{int(uitstootVliegtuig)} kg**")
    st.write(f"- 🔌 Elektriciteit: **{int(verbruikElektriciteit)} kg**")
    st.write(f"- 🥩 Vlees: **{int(consumptieVlees)} kg**")

    if totaal > 5202.5:
        st.write(f"⚠️ U stoot **{int(totaal - 5202.5)} kg meer** CO2 uit dan de gemiddelde Nederlander.")
    if totaal < 5202.5:
        st.write(f"✅ U stoot **{int(5202.5 - totaal)} kg minder** CO2 uit dan de gemiddelde Nederlander.")
    if totaal == 5202.5:
        st.write("🔄 U stoot precies evenveel CO2 uit als de gemiddelde Nederlander.")

    st.write(f"##### Uw totale CO2-uitstoot per jaar vergeleken met de gemiddelde Nederlander.")
    
    categorieën = ["Auto", "Trein", "Vliegtuig", "Elektriciteit", "Vlees"]
    UitstootGebruiker = [uitstootAuto, uitstootTrein, uitstootVliegtuig, verbruikElektriciteit, consumptieVlees]
    GemiddeldeUitstoot = [2500, 59.5, 1050, 540, 1053]

    fig, ax = plt.subplots(facecolor="lightgray")
    ax.set_facecolor("whitesmoke")
    bar_width = 0.4
    x = range(len(categorieën))

    ax.bar(x, UitstootGebruiker, width=bar_width, label="Uw verbruik", color="firebrick")
    ax.bar([i + bar_width for i in x], GemiddeldeUitstoot, width=bar_width, label="Gemiddeld verbruik", color="navy")
    ax.set_xticks([i + bar_width / 2 for i in x])
    ax.set_xticklabels(categorieën)
    ax.set_ylabel("CO2-uitstoot (kg)")
    ax.set_title("Uw jaarlijkse CO2-uitstoot")
    ax.legend()

    # Toon de grafiek in Streamlit
    st.pyplot(fig)
    
st.link_button("Hoe stoot ik minder CO2 uit? (Informatie)", "https://pure-energie.nl/kennisbank/6-tips-om-jouw-co2-footprint-te-verkleinen/")

