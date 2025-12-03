import streamlit as st
import asyncio
import aiohttp

API_KEY = "854f6451707d1d286bce772624b3527a"

weather_icons = {
    "clear": "☀️",
    "clouds": "☁️",
    "rain": "🌧️",
    "snow": "❄️",
    "mist": "🌫️",
    "haze": "🌫️",
    "drizzle": "🌦️",
    "thunderstorm": "⛈️",
}

async def get_weather(session, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    async with session.get(url) as resp:
        return {city: await resp.json()}

async def fetch_all(cities):
    async with aiohttp.ClientSession() as session:
        tasks = [get_weather(session, c) for c in cities]
        return await asyncio.gather(*tasks)

st.set_page_config(page_title="Weather App", page_icon="🌤", layout="centered")

st.title("🌤 Weather App")

city_input = st.text_input("Enter city names (comma separated)")

if st.button("Get Weather"):
    if not city_input:
        st.error("Please enter at least one city!")
    else:
        cities = [c.strip() for c in city_input.split(",")]
        results = asyncio.run(fetch_all(cities))

        for item in results:
            for city, data in item.items():
                if "main" not in data:
                    st.error(f"❌ {city} - Invalid City")
                    continue

                temp = data["main"]["temp"] - 273.15
                feels = data["main"]["feels_like"] - 273.15
                hum = data["main"]["humidity"]
                desc = data["weather"][0]["description"].title()
                wind = data["wind"]["speed"]
                cond = data["weather"][0]["main"].lower()

                icon = weather_icons.get(cond, "⛅")

                st.subheader(f"{icon} {city}")
                st.write(f"🌡 **Temperature:** {temp:.2f}°C")
                st.write(f"🤗 **Feels Like:** {feels:.2f}°C")
                st.write(f"💧 **Humidity:** {hum}%")
                st.write(f"⛅ **Condition:** {desc}")
                st.write(f"💨 **Wind:** {wind} m/s")
                st.markdown("---")

