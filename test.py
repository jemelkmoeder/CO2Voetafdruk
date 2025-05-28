import streamlit as st

st.title("CO2-voetafdruk Berekening")

auto = st.number_input("Hoeveel km reis jij per jaar met uw auto?")
trein = st.number_input("Hoeveel km reis jij per jaar met de trein?")
vliegtuig = st.number_input("Hoeveel km reis jij per jaar met het vliegtuig?")
elektriciteit = st.number_input("Hoeveel elektriciteit in kWh verbruikt u per maand?")
vlees = st.number_input("Hoeveel kilogram vlees consumeert u per jaar?")

if st.button("Bereken CO2-uitstoot"):
    uitstootAuto = 0.2 * auto
    uitstootTrein = 0.05 * trein
    uitstootVliegtuig = 0.25 * vliegtuig
    verbruikElektriciteit = 0.45 * 12 * elektriciteit
    consumptieVlees = 27 * vlees
    totaal = uitstootAuto + uitstootTrein + uitstootVliegtuig + verbruikElektriciteit + consumptieVlees

    st.write(f"Uw totale CO2-uitstoot per jaar: **{int(totaal)} kg**")
    st.write(f"Auto: {int(uitstootAuto)} kg")
    st.write(f"Trein: {int(uitstootTrein)} kg")
    st.write(f"Vliegtuig: {int(uitstootVliegtuig)} kg")
    st.write(f"Elektriciteit: {int(verbruikElektriciteit)} kg")
    st.write(f"Vlees: {int(consumptieVlees)} kg")

    if totaal > 5202.5:
        st.write(f"U stoot **{int(totaal - 5202.5)} kg meer** CO2 uit dan de gemiddelde Nederlander.")

    if totaal < 5202.5:
        st.write(f"U stoot **{int(5202.5 - totaal)} kg minder** CO2 uit dan de gemiddelde Nederlander.")