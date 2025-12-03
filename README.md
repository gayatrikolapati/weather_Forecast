🌤 Async Weather App

A modern and lightning-fast weather application built using Streamlit, asyncio, and aiohttp.
This app retrieves real-time weather updates for multiple cities simultaneously using asynchronous requests, resulting in faster performance and a smooth user experience.
Designed with a clean and minimal interface, it delivers essential weather information instantly.

🚀 Tech Stack 
Streamlit

A Python framework used to build the interactive web UI.
It allows rapid development, clean layouts, and deployment with just a GitHub repository.

asyncio

Python’s built-in asynchronous framework.
It enables multiple API requests to run together, instead of waiting for one request to finish before starting the next.

aiohttp

An asynchronous HTTP client library.
It lets the app make non-blocking API calls, improving speed and reducing waiting time.

OpenWeather API

A reliable and widely-used weather data provider.
It offers accurate real-time data such as temperature, humidity, weather description, and wind speed for any city.

⚡ Why Async? 
🔹 Parallel Requests

Instead of fetching weather for each city one by one, all city requests are made at the same time.

🔹 Faster Than Synchronous Code

Traditional requests block execution until one city’s weather loads.
Async avoids this delay, resulting in a major performance boost, especially for multiple cities.

🔹 Non-Blocking UI

The app remains responsive even when many requests are being processed.

🔹 Optimized for Network Operations

Async is especially powerful when fetching external data, as network latency is handled efficiently.

📌 Features
🔎 Search Multiple Cities

Users can enter multiple city names at once (comma-separated), and the app fetches their weather in a single click.

🌡 Live Weather Information

Displays:

Temperature

Feels-like temperature

Humidity

Weather description

Wind speed

All pulled instantly from the OpenWeather API.

🌤 Weather Condition Emojis

Each city is displayed with an emoji matching the weather condition (☀️, ☁️, 🌧️, etc.) for better readability and visual appeal.

🎨 Clean & Minimal UI

Built with Streamlit’s layout system for a simple, distraction-free interface.

⚡ High Performance

Async code ensures that results appear quickly, even when searching for many cities at once.

☁️ Streamlit Cloud Ready

The app can be deployed instantly with a shareable public link using Streamlit Cloud.
