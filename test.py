import unittest
from weather_class import WeatherStats
import os
import sqlite3

class TestWeatherStats(unittest.TestCase):
    """Unit tests for WeatherStats and database functionality."""

    def setUp(self):
        # Create a test instance of WeatherStats for Knoxville, TN on Oct 15, 2023
        self.weather = WeatherStats(
            latitude=35.960395,
            longitude=-83.921026,
            month=10,
            day=15,
            years=[2023]
        )
        # Fetch weather data and store it for testing
        self.weather_data = self.weather.fetch_weather_data()

    # -----------------------------
    # ✅ TEST 1: Verify API data retrieval (C2 validation)
    # -----------------------------
    def test_01_fetch_weather_data_returns_data(self):
        print("TEST 1: Checking if weather data is returned from API")
        self.assertTrue(self.weather_data, "No weather data returned")

    # -----------------------------
    # ✅ TEST 2: Verify temperature range validity
    # -----------------------------
    def test_02_average_temperature_within_range(self):
        print("TEST 2: Validating that average temperature is in expected range")
        avg_temp = self.weather_data[0]['mean_temperature']
        self.assertGreater(avg_temp, 30)
        self.assertLess(avg_temp, 110)

    # -----------------------------
    # ✅ TEST 3: Verify database insertion and query
    # -----------------------------
    def test_03_database_insertion_and_query(self):
        print("TEST 3: Verifying database insert and query returns expected result")
        db_path = "test_weather.db"
        if os.path.exists(db_path):
            os.remove(db_path)

        # Connect and insert dummy data
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data (
                            id INTEGER PRIMARY KEY,
                            latitude REAL, longitude REAL,
                            month INTEGER, day INTEGER, year INTEGER,
                            avg_temp REAL, min_temp REAL, max_temp REAL,
                            avg_wind_speed REAL, min_wind_speed REAL, max_wind_speed REAL,
                            sum_precipitation REAL, min_precipitation REAL, max_precipitation REAL)''')

        # Insert dummy row for testing
        cursor.execute('''INSERT INTO weather_data (latitude, longitude, month, day, year, avg_temp)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (35.960395, -83.921026, 10, 15, 2023, 75.0))
        conn.commit()

        # Query the dummy record and verify correctness
        cursor.execute("SELECT avg_temp FROM weather_data WHERE year = 2023")
        result = cursor.fetchone()
        self.assertEqual(result[0], 75.0)

        # Close and clean up
        conn.close()
        os.remove(db_path)

if __name__ == '__main__':
    unittest.main()
