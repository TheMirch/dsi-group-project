<h1 align = 'center'>Bush Pilot Safety</h1>

<h4 align = 'center'>AUTHORS</h4>
<center>Muhammad Hassan, Sophia Joseph, Mike Minikowski, Lisa Paul, Nolan Smurro</center>

 <br><hr><br>




## Problem Statement
> Can statistically significant contributing factors to serious aviation accidents among Alaskan Bush Pilots be identified?

## Executive Summary
> This project seeks to analyze data related to aviation incidents involving single-engine aircraft in Alaska, with a focus on those leading to  fatalities. By understanding the primary factors contributing to these incidents, we hope to be able to contribute to recommendations for safety initiatives to further protect Alaskan aviators in the general aviation community.

> Our work for the Alaska Airmen’s Association (AAA) is rooted in the goal of promoting effective emergency response and preventing fatal accidents. The AAA, a nonprofit established in 1951, is dedicated to promoting general aviation, enhancing safety, and supporting initiatives that benefit pilots. Our efforts aim to support their mission of advocating for access and safety infrastructure across the state. We seek to provide the AAA with our findings to support their advocation efforts in the upcoming 2024 calendar year.


## About Alaskan Bush Pilots
> Alaskan Bush Pilots are integral in communites throughout Alaska, demonstrating resilience and expertise while navigating the vast and rugged landscapes of Alaska. Often piloting single-engine light aircraft, these aviators must handle unpredictable weather conditions and challenging landing terrains. Their missions extend beyond conventional flight. They serve as the primary or only means of transportation for delivery and essential services to isolated communities. Additionally, Alaskan Bush Pilots play a vital role in search and rescue operations. 



 <br><hr><br>
## File Directory / Table of Contents
This is an alphabetical list of the repository's directory and file structure. 

```
- README.md
- code
  - 01_cleaning.ipynb
  - 02_eda.ipynb
  - 03_nlp.ipynb
  - 04_model_glm.ipynb
  - 05_model_logreg_event_time_of_day.ipynb
  - 06_model_logreg_occurred_near_airport.ipynb
  - 07_model_logreg_event_time_of_day.ipynb
- datasets
  - data_cleaned
    - alaska_single_engine_clean.csv
  - data_raw
    - alaska_single_engine.csv
- images
  - probable_cause.png
- pickles
  - logreg_occurred_near_airport-has_fatal_injury.pkl
  - logreg_weather_condition-has_fatal_injury.pkl
- presentation
  - alaskan_bush_pilot_safety.pdf
- results
  - glm_pvalues.csv
  - logreg_occurred_near_airport-has_fatal_injury_coef.csv
  - logreg_weather_condition-has_fatal_injury_coef.csv
```


## Software Requirements 
- GeoPandas
- Jupyter Notebook
- Matplotlib.pyplot
- NumPy
- Pandas
- Pickle
- Scikit-Learn (sklearn)
- Statsmodels.api


## Data Dictionary
<br><hr><br>

| Feature          | Description                             | Details |
|----------------------|-----------------------------------------|---------|
| EventId              | Unique Identification for Each Event    | Each event is assigned a unique 14-character alphanumeric code in the database. This code is used to reference all database records. |
| InvestigationType    | Type of Event                           | Refers to a regulatory definition of the event severity, combining the highest level of injury and aircraft damage. |
| AccidentNumber       | NTSB Number                             | Each accident/incident is assigned a unique case number by the NTSB. The number includes information about the office, fiscal year, investigation category, and sequence. |
| EventDate            | Event Date                              | The date of the event in MM/DD/YYYY format. |
| Location             | Event Location Nearest City            | The city or place location closest to the site of the event. |
| Country              | Event Country                           | The country where the event took place. |
| Latitude             | Event Location Latitude                 | Latitude coordinates of the event site in degrees and decimal degrees. |
| Longitude            | Event Location Longitude                | Longitude coordinates of the event site in degrees and decimal degrees. |
| AirportCode          | Event Location Nearest Airport ID      | Airport code if the event occurred near an airport or involved aircraft taking off from or on approach to an airport. |
| AirportName          | Event Location Airport                  | Airport name if the event occurred near an airport or involved aircraft taking off from or on approach to an airport. |
| InjurySeverity       | Event Highest Injury                    | Indicates the highest level of injury among all injuries sustained during the event. |
| AircraftDamage       | Damage                                  | Indicates the severity of damage to the accident aircraft. |
| AircraftCategory     | Aircraft Category                       | The category of the involved aircraft as per certification and airmen definitions. |
| RegistrationNumber   | Aircraft Registration Number             | The full registration (tail) number of the involved aircraft, including the ICAO country prefix. |
| Make                 | Aircraft Manufacturer's Full Name       | Name of the manufacturer of the involved aircraft. |
| Model                | Aircraft Model                          | The alphanumeric aircraft model code, including series or derivative identifiers. |
| AmateurBuilt         | Aircraft is a homebuilt (Y/N)           | Indicates whether the aircraft is homebuilt (Yes/No). |
| NumberOfEngines      | Number of Engines                       | The total number of engines on the accident aircraft. |
| EngineType           | Engine Type                             | Type of engine(s) on the involved aircraft. |
| FARDescription       | Federal Aviation Reg. Part              | The regulation part (14 CFR) or authority under which the aircraft was operating at the time of the accident. |
| Schedule             | Indicates whether an air carrier operation was scheduled or not | Specifies if the accident aircraft was operating as a "scheduled or commuter" air carrier or as a "non-scheduled or air taxi" carrier. |
| PurposeOfFlight      | Type of Flying (Per_Bus / Primary)      | The primary purpose of flight under 14 CFR part 91, 103, 133, or 137 for the accident aircraft. |
| AirCarrier           | Operator Name & Operator Is Doing Business As | The full name of the operator of the accident aircraft, including carrier, business, or code share names. |
| TotalFatalInjuries   | Injury Total Fatal                      | The total number of fatal injuries resulting from the event. |
| TotalSeriousInjuries | Injury Total Serious                    | The total number of serious injuries resulting from the event. |
| TotalMinorInjuries   | Injury Total Minor                      | The total number of minor injuries resulting from the event. |
| TotalUninjured       | Non-Injury Total                        | The total number of individuals who were not injured in the event. |
| WeatherCondition     | Basic weather conditions                | The basic weather conditions at the time of the event. |
| BroadPhaseOfFlight   | Phase of Flight                        | The phase of flight in which the event took place. |
| ReportStatus         | Latest Report Level                    | The furthest level to which a report has been completed. |
| PublicationDate      | Publication data of the Latest Report Level | The date on which the previous column was published to the web. |



<br><hr><br>
## Conclusions and Recommendations
Based on the key insights from our project, we can offer the following recommendations to the Alaska Airmen's Association, to address a spectrum of factors, ultimately improving aviation safety among Alaskan Bush Pilots:

### Weather Condition/ Visibility
> **Findings:**  
Our findings indicate that the effect of VMC conditions can lead to a 43.8% decrease in the odds of fatal injury in accidents compared to Instrument Meteorological Conditions (IMC) all else held equal.

> **Recommendations:** 
> - Encourage members to seek and maintain their instrument
ratings.
> - Promote workshops and further resources related to
operating in IMC conditions.
> - Promote the use of weather forecasting and flight planning
tools.
> - Advocate for improvements in air traffic control procedures.

### Airport Proximity
> **Findings:**  
Our findings indicate that the effect of accidents occuring at or within 3 miles of an airport leads to an increase in odds of fatal injury by 11.1%.

> **Recommendations:** 
> - Promote the use of ground proximity warning systems
(GPWS).
> - Advocate for improvements to airport infrastructure and
runway conditions.
> - Work with airport authorities to develop and implement safety
procedures for low-altitude operations.

### Time of Day
> **Findings:**  
Our findings indicate that the effect of flying at night contributes to a 9.0% increase in fatal injury in accidents compared to flying in the morning, all else held equal.

> **Recommendations:** 
> - Promote workshops and resources on night flying safety.
> - Promote the use of night vision goggles (NVGs) and other
night flying equipment and training where applicable.

### General Recommendations:
> - Host workshops or seminars on fatal crash prevention.
> - Develop and distribute educational materials on fatal crash
risk factors.

<br><hr><br>
## Sources
- [NTSB Aviation Investigation Database](https://www.ntsb.gov/Pages/AviationQueryV2.aspx)
- [Alaska Airmen's Association](https://alaskaairmen.org/about/)
- [The lifeline of flying: the pilots connecting remote communities in Alaska - The Guardian](https://www.theguardian.com/artanddesign/2023/may/22/its-almost-spiritual-the-female-pilots-connecting-remote-alaska#:~:text=Today%2C%20flying%20is%20part%20of,else%20in%20the%20United%20States.&text=A%20group%20of%20pilots%20fly,River%20Valley%20near%20Palmer%2C%20Alaska.)