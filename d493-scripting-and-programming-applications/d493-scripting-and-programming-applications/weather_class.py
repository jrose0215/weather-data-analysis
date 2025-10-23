import requests

# C1. Create a Class with variables for location and date

class WeatherStats:
    def __init__(self, latitude, longitude, month, day, years):

        # Location Info
        self.latitude = latitude
        self.longitude = longitude

        # Date info
        self.month = month
        self.day = day
        self.years = years

        # Temperature (Fahrenheit)
        self.average_temp = None
        self.min_temp = None
        self.max_temp = None

        # Wind speed (Miles per hour)
        self.average_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None

        # Precipitation (inches)
        self.sum_precipitation = None
        self.min_precipitation = None
        self.max_precipitation = None

    # C2. Create method using "Weather API" web link to pull data for chosen location and data.

    def fetch_weather_data(self):
        """Fetch temp, wind, and precip for 5 years — store results in instance variables"""
        temp_values = []
        wind_values = []
        precip_values = []

        for year in self.years:
            url = (
                f"https://archive-api.open-meteo.com/v1/archive?"
                f"latitude={self.latitude}&longitude={self.longitude}"
                f"&start_date={year}-{self.month:02d}-{self.day:02d}"
                f"&end_date={year}-{self.month:02d}-{self.day:02d}"
                f"&daily=temperature_2m_mean,wind_speed_10m_max,precipitation_sum"
                f"&temperature_unit=fahrenheit&wind_speed_unit=mph"
                f"&precipitation_unit=inch&timezone=America/New_York"
            )

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                try:
                    temp = data['daily']['temperature_2m_mean'][0]
                    wind = data['daily']['wind_speed_10m_max'][0]
                    precip = data['daily']['precipitation_sum'][0]

                    print(f"{year}: Temp {temp}°F | Wind {wind} mph | Precip {precip} in")

                    temp_values.append(temp)
                    wind_values.append(wind)
                    precip_values.append(precip)
                except (KeyError, IndexError):
                    print(f"Missing data for {year}")
            else:
                print(f"Failed to fetch data for {year}: {response.status_code}")

        if temp_values:
            self.average_temp = sum(temp_values) / len(temp_values)
            self.min_temp = min(temp_values)
            self.max_temp = max(temp_values)

        if wind_values:
            self.average_wind_speed = sum(wind_values) / len(wind_values)
            self.min_wind_speed = min(wind_values)
            self.max_wind_speed = max(wind_values)

        if precip_values:
            self.sum_precipitation = sum(precip_values)
            self.min_precipitation = min(precip_values)
            self.max_precipitation = max(precip_values)

        years_data = []
        for i, year in enumerate(self.years):
            years_data.append({
                "year": year,
                "mean_temperature": temp_values[i] if i < len(temp_values) else None,
                "max_wind_speed": wind_values[i] if i < len(wind_values) else None,
                "precipitation_sum": precip_values[i] if i < len(precip_values) else None
            })

        return years_data