<h1 align = 'center'>Bush Pilot Safety</h1>

<h4 align = 'center'>AUTHORS</h4>
<center>Muhammad Hassan, Sophia Joseph, Mike Minikowski, Lisa Paul, Nolan Smurro</center>

 <br><hr><br>




### Problem Statement
> Can we identify significant contributing factors to serious aviation accidents among Alaskan Bush Pilots?

### Executive Summary
> This project seeks to analyze data related to aviation incidents involving single-engine aircraft in Alaska, with a focus on those leading to serious injuries or fatalities. By understanding the primary factors contributing to these incidents, we hope to develop targeted safety initiatives, enhance pilot training programs, and implement effective preventive measures. 

> Our collaboration with the Alaska Airmen’s Association (AAA) is rooted in the goal of promoting effective emergency response and preventing accidents. The AAA, a nonprofit established in 1951, is dedicated to promoting general aviation, enhancing safety, and supporting initiatives that benefit pilots. Our joint efforts aim to make flying safer for Alaskan Bush Pilots and the communities they serve.


### About Alaskan Bush Pilots
> Alaskan Bush Pilots are essential contributors: demonstrating resilience and expertise while navigating the vast and rugged landscapes of Alaska. Often piloting single-engine light aircraft, these aviators must handle unpredictable weather conditions and challenging landing terrains. Their missions extend beyond conventional flight: they serve as the primary or only means of transportation for delivery and essential services to isolated communities. Additionally, Alaskan Bush Pilots play a vital role in search and rescue operations. 



 <br><hr><br>
## File Directory / Table of Contents
This is an alphabetical list of the repository's directory and file structure. 


- README.md
- code
  - 01_cleaning.ipynb
  - 02_eda.ipynb
  - 03_nlp.ipynb
  - 04_model_glm.ipynb
  - 05_model_logreg.ipynb
  - 06_model_logreg.ipynb
  - 07_model_logreg.ipynb
- datasets
  - alaska_single_engine_clean.csv
  - data_cleaned
    - alaska_single_engine_clean.csv
  - data_raw
    - alaska_single_engine.csv
- images
  - Confusion matrix based on NLP.png
  - Damage_by_injury.png
  - Screenshot 2023-11-08 134415.png
  - Screenshot 2023-11-08 140405.png
  - Sheet 1.png
  - Sorted p value.png
  - TSNE Gorg.png
  - World of ave.png
  - incidents_by_injury_level.png
  - incidents_by_season.png
  - injuries_by_operator.png
  - injuries_by_purpose.png
  - injuries_by_tod.png
  - probable_cause.png
- pickles
  - logreg_occurred_near_airport-has_fatal_injury.pkl
  - logreg_weather_condition-has_fatal_injury.pkl
- presentation
  - alaskan_bush_pilot_safety.pdf
- results
  - glm_pvalues3_time_of_day_y_as_severe_and_fatal_acc836.csv
  - logreg_occurred_near_airport-has_fatal_injury_coef.csv
  - logreg_weather_condition-has_fatal_injury_coef.csv
- scratch
  - Moe_file_listing.ipynb
  - Moe_file_using_alaska_sec.ipynb
  - Moe_file_using_alaska_secV2.ipynb
  - Moe_nolan_model_logreg_weather_condition-has_fatal_injury.ipynb
  - Moe_streamlit.py
  - Use for Viz
    - alaska_single_engine_clean.csv
  - alaska_single_engine_clean_camel.csv
  - aviation_data.csv
  - example-filetree.txt
  - feature_importances.csv
  - glm_pvalues1_initialfeatureset_y_as_severe_and_fatal_acc835.csv
  - glm_pvalues2_city_and_aircraft_family_y_as_severe_and_fatal_acc838.csv
  - glm_pvalues4_am_pm_y_as_severe_and_fatal_acc838.csv
  - logreg_coef
    - nolan_logreg_aircraft_family-has_fatal_injury_coef.csv
    - nolan_logreg_amateur_built-has_fatal_injury_coef.csv
    - nolan_logreg_city-has_fatal_injury_coef.csv
    - nolan_logreg_event_am_pm-has_fatal_injury_coef.csv
    - nolan_logreg_event_hour-has_fatal_injury_coef.csv
    - nolan_logreg_event_season-has_injury_coef.csv
    - nolan_logreg_event_time_of_day-has_fatal_injury_coef.csv
    - nolan_logreg_occurred_near_airport-has_aircraft_damage_coef.csv
    - nolan_logreg_occurred_near_airport-has_fatal_injury_coef.csv
    - nolan_logreg_occurred_near_airport-has_injury_coef.csv
    - nolan_logreg_purpose_of_flight-has_fatal_injury_coef.csv
    - nolan_logreg_weather_condition-has_aircraft_damage_coef.csv
    - nolan_logreg_weather_condition-has_fatal_injury_coef.csv
    - nolan_logreg_weather_condition-has_injury_coef.csv
  - mike_atb1.csv
  - mike_atb2.csv
  - mike_eda.ipynb
  - nolan_cleaning_comma_exploder.ipynb
  - nolan_eda.ipynb
  - nolan_model.ipynb
  - nolan_model_logreg_aircraft_family-has_fatal_injury.ipynb
  - nolan_model_logreg_amateur_built-has_fatal_injury.ipynb
  - nolan_model_logreg_city-has_fatal_injury.ipynb
  - nolan_model_logreg_event_am_pm-has_fatal_injury.ipynb
  - nolan_model_logreg_event_hour-has_fatal_injury.ipynb
  - nolan_model_logreg_occurred_near_airport-has_aircraft_damage.ipynb
  - nolan_model_logreg_occurred_near_airport-has_injury.ipynb
  - nolan_model_logreg_purpose_of_flight-has_fatal_injury.ipynb
  - nolan_model_logreg_weather_condition-has_aircraft_damage.ipynb
  - nolan_model_logreg_weather_condition-has_injury.ipynb
  - pickles
    - mike_logreg.pkl
    - nolan_logreg_aircraft_family-has_fatal_injury.pkl
    - nolan_logreg_amateur_built-has_fatal_injury.pkl
    - nolan_logreg_city-has_fatal_injury.pkl
    - nolan_logreg_event_am_pm-has_fatal_injury.pkl
    - nolan_logreg_event_hour-has_fatal_injury.pkl
    - nolan_logreg_event_time_of_day-has_fatal_injury.pkl
    - nolan_logreg_occurred_near_airport-has_aircraft_damage.pkl
    - nolan_logreg_occurred_near_airport-has_fatal_injury.pkl
    - nolan_logreg_occurred_near_airport-has_injury.pkl
    - nolan_logreg_purpose_of_flight-has_fatal_injury.pkl
    - nolan_logreg_weather_condition-has_aircraft_damage.pkl
    - nolan_logreg_weather_condition-has_fatal_injury.pkl
    - nolan_logreg_weather_condition-has_injury.pkl
  - probable_cause.png
  - sophia_eda.ipynb
  - sophia_glm.ipynb
```


## Software Requirements  
- Jupyter Notebook
- Matplotlib.pyplot
- NumPy
- Pandas
- Pickle
- Scikit-Learn (sklearn)
- Statsmodels.api


### Data Dictionary
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
### Conclusions and Recommendations
> Based on the key insights from our project, we can offer the following key recommendations to to the AAA, to address a spectrum of factors, ultimately improving aviation safety among Alaskan Bush Pilots:

> **Weather Condition Awareness:**  Prioritize flying in Visual Meteorological Conditions (VMC) whenever possible, to significantly reduce the risk of fatal injuries. Our findings indicate that flying in VMC conditions can lead to a 43.8% decrease in the odds of fatal injury compared to flying in Instrument Meteorological Conditions (IMC). Additionally, we suggest the AAA strongly encourages pilots to get and maintain their instrument ratings, and advocates for training and further resources on flying in IMC conditions. We also recommend promoting the use of weather forecasting and flight planning tools to improve weather condition awareness. 

> **Avoidance of Airport Proximity:**  Exercise caution when flying near airports, especially within a 3-mile radius. Our analysis reveals an 11.1% increase in the likelihood of fatal injuries occurring in such circumstances. Maintaining a safe distance from airports during flights can help mitigate this risk. We also advocate for improvements in air traffic control procedures for IMC conditions. Additionally, we recommend advocating for the utilization of ground proximity warning systems (GPWS), improvements in airport signage and lighting, and collaborative work with airport authorities to develop safety procedures for low-altitude operations. 

> **Time of Day Consideration:** Be mindful of the time of day when planning flights. Flying at nighttime carries a 9% higher risk of fatal injuries compared to morning flights. Where possible, adjusting flight schedules to minimize nighttime operations could contribute to a safer flying environment. Additionally, the AAA can encourage members to get and maintain their night flying proficiency, recommend training and resources on night flying safety, and promote the use of night vision goggles (NVGs) and other night flying equipment.


> **Other Safety Measures:** Hosting workshops or seminars on fatal crash prevention and creating educational materials on fatal crash risk factors will further contribute to fostering a safer flying environment for Alaskan Bush Pilots and the communities they serve.