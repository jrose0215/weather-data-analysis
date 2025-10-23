# WGU D493 Scripting and Programming - Applications
# Weather Data Analysis Project 

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Program Structure](#program-structure)
- [Inputs](#inputs)
- [Sample Output](#sample-output)
- [Testing](#testing)
- [Notes](#notes)
- [References](#references)

---

## Overview

This Python project collects historical weather data for Knoxville, TN on October 31st over a five year span (2019–2023), using the [Open-Meteo Archive API](https://open-meteo.com/en/docs). It stores the data in an SQLite database using SQLAlchemy and shows key weather statistics including temperature, wind speed, and precipitation.

---

## Dependencies

- Python 3.10+
- `requests` - calls API
- `SQLAlchemy` - Python SQL toolkit and Object Relational Mapper (ORM)
- `tabulate` - display data in various tabular formats
- `pytests` - used to test functionality

---

## Program Structure

- `main.py`: 
    * Runs the weather data collection and inserts results into the database.
    * Defines the SQLAlchemy ORM class and handles database creation and insertion.
- `weather_class.py`: Contains the `WeatherStats` class responsible for API calls and processing data.
- `test.py`: Unit tests for ensuring correctness of methods and calculations.

---

## Inputs

- **City:** Knoxville, TN
- **Latitude:** 35.960395
- **Longitude:** -83.921026
- **Date:** October 31st
- **Years:** 2019, 2020, 2021, 2022, 2023

---

## Sample Output

```
2019: Temp 56.6°F | Wind 19.5 mph | Precip 0.591 in
2020: Temp 49.7°F | Wind 6.5 mph | Precip 0.0 in
2021: Temp 54.4°F | Wind 7.0 mph | Precip 0.0 in
2022: Temp 62.2°F | Wind 12.6 mph | Precip 0.492 in
2023: Temp 48.4°F | Wind 9.7 mph | Precip 0.0 in
```

## Testing
Testing is ran to confirm the following:
- Checking if weather data is returned from API
- Validating that average temperature is in expected range
- Verifying database insert and query returns expected result

To test, run the following:

```bash
python -m unittest test.py
```

## Notes

- Data is retrieved via Open-Meteo API (no API key required).
- The database is recreated with each run unless modified.

---
## References
Per listed on the Open Mateo website:
- Zippenfenig, Patrick. Open-Meteo.com Weather API. Zenodo, 2023. doi:10.5281/ZENODO.7970649

- Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023). ERA5 hourly data on single levels from 1940 to present [Data set]. ECMWF. https://doi.org/10.24381/cds.adbb2d47

- Muñoz Sabater, J. (2019). ERA5-Land hourly data from 2001 to present [Data set]. ECMWF. https://doi.org/10.24381/CDS.E2161BAC

- Schimanke, S., Ridal, M., Le Moigne, P., Berggren, L., Undén, P., Randriamampianina, R., Andrea, U., Bazile, E., Bertelsen, A., Brousseau, P., Dahlgren, P., Edvinsson, L., El Said, A., Glinton, M., Hopcsh, S., Isaksson, L., Mladek, R., Olsson, E., Verrelle, A., Wang, Z.Q. (2021). CERRA Sub-Daily Regional Reanalysis Data for Europe on Single Levels from 1984 to Present. ECMWF. doi:10.24381/CDS.622A565A