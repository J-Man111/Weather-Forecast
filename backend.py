import streamlit as st
import requests

API_KEY = "c91fafc9ff578769af657983cf0b9b2b"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    data = response.json()
    filtered_data = []
    try:
        filtered_data = data["list"]
    except KeyError:
        st.subheader("Please enter a valid city.")
        
    nr_values = 8 * forecast_days
    if len(filtered_data) != 0:
        filtered_data = filtered_data[:nr_values]
        return filtered_data     
    else:
        return []
    
if __name__ =="__main__":
    print(get_data(place="Tokyo", forecast_days=3))