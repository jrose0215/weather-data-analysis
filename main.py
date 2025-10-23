# Importing all necessary tools to interact with the database that will be created.
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from weather_class import WeatherStats
import sqlite3
from tabulate import tabulate

# Location - Knoxville TN, Date - October 31, Years - 2019 to 2023
latitude = 35.960395
longitude = -83.921026
month = 10
day = 31
years = [2019, 2020, 2021, 2022, 2023]

# C3. Creating an instance of the WeatherData class.
weather = WeatherStats(latitude=latitude, longitude=longitude, month=month, day=day, years=years)
weather_by_year = weather.fetch_weather_data()

base = declarative_base()


# C4. Create a second class using SQLAlchemy ORM module
class WeatherDBRecord(base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    years = Column(Integer, nullable=False)

    # Weather data.
    average_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    average_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    precipitation_sum = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)


# Creating the SQLite engine and table.
engine = create_engine('sqlite:///weather_data.db')
base.metadata.drop_all(engine)  # Drop table if it exists.
base.metadata.create_all(engine)  # Recreate table.

# Create a session.
Session = sessionmaker(bind=engine)
session = Session()

# Insert weather data for each year into the database.
for year_data in weather_by_year:
    record = WeatherDBRecord(
        latitude=latitude,
        longitude=longitude,
        month=month,
        day=day,
        years=year_data['year'],
        average_temp=year_data['mean_temperature'],
        min_temp=year_data['mean_temperature'],
        max_temp=year_data['mean_temperature'],
        average_wind_speed=year_data['max_wind_speed'],
        min_wind_speed=year_data['max_wind_speed'],
        max_wind_speed=year_data['max_wind_speed'],
        precipitation_sum=year_data['precipitation_sum'],
        min_precipitation=year_data['precipitation_sum'],
        max_precipitation=year_data['precipitation_sum']
    )
    session.add(record)

session.commit()
session.close()

print("Weather data inserted successfully into the database.")


# Defining method to query the table.

def display_weather_table(latitude, longitude, month, day):
    # Connecting to SQLite database.
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()

    # SQL query to retrieve the data for Knoxville, TN on October 31st.
    query = """
    SELECT * FROM weather_data
    WHERE latitude = ? AND longitude = ?
    AND month = ? AND day = ?
    ORDER BY years ASC
    ;
    """

    cursor.execute(query, (latitude, longitude, month, day))
    rows = cursor.fetchall()

    # Defining table headers.

    if rows:
        headers = ["Year", "Month", "Day", "Average Temp (°F)", "Min Temp (°F)", "Max Temp (°F)", "Average Wind Speed (mph)",
                   "Min Wind Speed (mph)", "Max Wind Speed (mph)", "Precipitation (inches)"
                   ]

        # Formatting the data into a table.
        table_data = []
        for row in rows:
            table_data.append([
                row[5],
                row[3],
                row[4],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12]
            ])

        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    else:
        print("No data available.")

    cursor.close()
    connection.close()


# Calling the query function to display the data.
display_weather_table(latitude, longitude, month, day)