import streamlit as st
import requests
import matplotlib.pyplot as plt

st.title("Weather App")

city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    api_key = "acb215dfeba36105cd494ca3f9913c27"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()

        # Show weather info
        st.subheader(f"📍 Weather in {city.title()}")
        st.write(f"**Condition:** {weather}")
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Humidity:** {humidity}%")

        # Bar chart
        labels = ['Temperature (°C)', 'Humidity (%)']
        values = [temp, humidity]
        colors = ['orange', 'skyblue']

        fig, ax = plt.subplots()
        bars = ax.bar(labels, values, color=colors)

        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}', ha='center')

        ax.set_title(f"Weather Stats for {city.title()}")
        ax.set_ylim(0, max(values) + 20)
        st.pyplot(fig)

    else:
        st.error("City not found or error in API call.")
