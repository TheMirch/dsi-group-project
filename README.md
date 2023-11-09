<h1 align = 'center'>Bush Pilot Safety</h1>

<h4 align = 'center'>AUTHORS</h4>
<center>Muhammad Hassan, Sophia Joseph, Mike Minikowski, Lisa Paul, Nolan Smurro</center>

 <br><hr><br>




### Problem Statement
> Can we identify significant contributing factors to serious aviation accidents among Alaskan Bush Pilots?

### Executive Summary
> This project seeks to analyze data related to aviation incidents involving single-engine aircraft in Alaska, with a focus on those leading to serious injuries or fatalities. By understanding the primary factors contributing to these incidents, we hope to develop targeted safety initiatives, enhance pilot training programs, and implement effective preventive measures. 

> Our collaboration with the Alaska Airmen’s Association is rooted in the goal of promoting effective emergency response and preventing accidents. The Alaska Airmen’s Association, a nonprofit established in 1951, is dedicated to promoting general aviation, enhancing safety, and supporting initiatives that benefit pilots. Our joint efforts aim to make flying safer for Alaskan Bush Pilots and the communities they serve.


### About Alaskan Bush Pilots
> Alaskan Bush Pilots are essential contributors: demonstrating resilience and expertise while navigating the vast and rugged landscapes of Alaska. Often piloting single-engine light aircraft, these aviators must handle unpredictable weather conditions and challenging landing terrains. Their missions extend beyond conventional flight: they serve as the primary or only means of transportation for delivery and essential services to isolated communities. Additionally, Alaskan Bush Pilots play a vital role in search and rescue operations. 



 <br><hr><br>
## File Directory / Table of Contents
This is an alphabetical list of the repository's directory and file structure. 
> To follow along, start with "code/Nolan_cleaning.ipynb". Then, because our work was parallelized, the next step might be any other Jupyter Notebook files in the code directory.



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
> Based on the key insights from our project, we can offer the following key recommendations to improve aviation safety among Alaskan Bush Pilots:

> **Weather Condition Awareness:**  Prioritize flying in Visual Meteorological Conditions (VMC) whenever possible, to significantly reduce the risk of fatal injuries. Our findings indicate that flying in VMC conditions can lead to a 43.8% decrease in the odds of fatal injury compared to flying in Instrument Meteorological Conditions (IMC).

> **Avoidance of Airport Proximity:**  Exercise caution when flying near airports, especially within a 3-mile radius. Our analysis reveal an 11.1% increase in the likelihood of fatal injuries occurring in such circumstances. Maintaining a safe distance from airports during flights can help mitigate this risk.

> **Time of Day Consideration:** Be mindful of the time of day when planning flights. Flying at nighttime carries a 9% higher risk of fatal injuries compared to morning flights. Where possible, adjusting flight schedules to minimize nighttime operations could contribute to a safer flying environment.
