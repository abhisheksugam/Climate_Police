# Data Description

We have two datasets for this project:

### US Pollution data
* **Name**: pollution_us_2000_2016.csv
* **Description**: This dataset deals with pollution in the U.S.. It contains four major pollutants (Nitrogen Dioxide, Sulphur Dioxide, Carbon Monoxide and Ozone) for every day from 2000 - 2016.
* **Size**: 1746661 rows × 29 columns
* **Fields**: 28 feilds.
    1. State Code : The code allocated by US EPA to each state
    2. County code : The code of counties in a specific state allocated by US EPA
    3. Site Num : The site number in a specific county allocated by US EPA
    4. Address: Address of the monitoring site
    5. State : State of monitoring site
    6. County : County of monitoring site
    7. City : City of the monitoring site
    8. Date Local : Date of monitoring

    The four pollutants (NO2, O3, SO2 and O3) each has 5 specific columns. For instance, for NO2:
        1. NO2 Units : The units measured for NO2
        2. NO2 Mean : The arithmetic mean of concentration of NO2 within a given day
        3. NO2 AQI : The calculated air quality index of NO2 within a given day
        4. NO2 1st Max Value : The maximum value obtained for NO2 concentration in a given day
        5. NO2 1st Max Hour : The hour when the maximum NO2 concentration was recorded in a given day

### Earth Surface Temperature Data
* **Names**:
    GlobalTemperatures.csv
    GlobalLandTemperaturesByCountry.csv
    GlobalLandTemperaturesByState.csv
    GlobalLandTemperaturesByMajorCity.csv
    GlobalLandTemperaturesByCity.csv
* **Description**: The data is from a newer compilation put together by the Berkeley Earth, which is affiliated with Lawrence Berkeley National Laboratory. The Berkeley Earth Surface Temperature Study combines 1.6 billion temperature reports from 16 pre-existing archives.
* **Size**:
    * GlobalTemperatures: 3192 rows × 9 columns
    * GlobalLandTemperaturesByCountry: 577462 rows × 4 columns
    * GlobalLandTemperaturesByState: 645675 rows × 5 columns
    * GlobalLandTemperaturesByMajorCity: 239177 rows × 7 columns
    * GlobalLandTemperaturesByCity: 8599212 rows × 7 columns
* **Fields**: In the GlobalTemperatures data, for example, we have
    1. Date: starts in 1750 for average land temperature and 1850 for max and min land temperatures and global ocean and land temperatures
    * LandAverageTemperature: global average land temperature in celsius
    * LandAverageTemperatureUncertainty: the 95% confidence interval around the average
    * LandMaxTemperature: global average maximum land temperature in celsius
    * LandMaxTemperatureUncertainty: the 95% confidence interval around the maximum land temperature
    * LandMinTemperature: global average minimum land temperature in celsius
    * LandMinTemperatureUncertainty: the 95% confidence interval around the minimum land temperature
    * LandAndOceanAverageTemperature: global average land and ocean temperature in celsius
    * LandAndOceanAverageTemperatureUncertainty: the 95% confidence interval around the global average land and ocean temperature

    Other data have similar fields, with some geographic information depending on the the specific data.

We can easily create a subset of data for unit test, since we can use `groupby` function provided by `pandas` to test different cases for each unit.
