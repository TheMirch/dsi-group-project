# dsi-group-project

## Data Dictionary
| Column Name          | Description                             | Details |
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