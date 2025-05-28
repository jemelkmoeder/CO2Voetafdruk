import streamlit as st

st.title("CO2-voetafdruk Berekening")

# Invoervelden
auto = st.number_input("Hoeveel km reis jij per jaar met uw auto?", min_value=0, value=0, step=1)
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

    st.write(f"### Uw totale CO2-uitstoot per jaar: **{int(totaal)} kg**"
