from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Tempurature", "Sky",))
st.subheader(f"{option} for the next {days} days in {place}")

#Get the temperature/sky data
if place:
    filtered_data = get_data(place, days)

    if len(filtered_data) > 0:

        if option == "Tempurature":
            #Create a temperature plot
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [
                datetime.fromtimestamp(dict["dt"], tz=timezone.utc)
                .astimezone(ZoneInfo("America/Denver"))
                .replace(tzinfo=None)
                for dict in filtered_data
            ]
            figure = px.line(x=dates, y=temperatures,
                            labels={"x":"Date", "y": "Temperature (F)"})
            figure.update_xaxes(tickformat="%I:%M %p<br>%b %-d, %Y")
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"]
                            for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)