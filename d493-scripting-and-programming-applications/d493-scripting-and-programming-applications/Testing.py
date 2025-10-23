# Printing the calculated results to verify it is working
# Used after calling fetch_weather_data

print("\n--- 5-Year Weather Summary ---")
print(f"Average Temperature: {weather.average_temp:.2f}°F")
print(f"Min Temperature: {weather.min_temp:.2f}°F")
print(f"Max Temperature: {weather.max_temp:.2f}°F")

print(f"Average Wind Speed: {weather.average_wind_speed:.2f} mph")
print(f"Min Wind Speed: {weather.min_wind_speed:.2f} mph")
print(f"Max Wind Speed: {weather.max_wind_speed:.2f} mph")

print(f"Total Precipitation: {weather.sum_precipitation:.2f} in")
print(f"Min Precipitation: {weather.min_precipitation:.2f} in")
print(f"Max Precipitation: {weather.max_precipitation:.2f} in")