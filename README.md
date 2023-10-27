# dsi-group-project

## Data Dictionary
| Column Name            | Data Type | Description                                            |
|------------------------|-----------|--------------------------------------------------------|
| NtsbNo                 | object    | The NTSB number for the accident                       |
| EventType              | object    | The type of event or accident                           |
| Mkey                   | int64     | An identifier for the accident                         |
| EventDate              | object    | The date and time of the accident                      |
| City                   | object    | The city where the accident occurred                   |
| State                  | object    | The state where the accident occurred                  |
| Country                | object    | The country where the accident occurred                |
| ReportNo               | object    | The report number associated with the accident         |
| N                      | object    | An identifier (unclear without additional context)    |
| HasSafetyRec           | bool      | Indicates whether the accident has a safety recommendation |
| ReportType             | object    | The type of report                                      |
| OriginalPublishDate    | object    | The date when the report was originally published      |
| HighestInjuryLevel     | object    | The highest level of injury sustained in the accident  |
| FatalInjuryCount       | int64     | The count of fatal injuries in the accident            |
| SeriousInjuryCount     | int64     | The count of serious injuries in the accident          |
| MinorInjuryCount       | int64     | The count of minor injuries in the accident            |
| ProbableCause          | object    | A description of the probable cause of the accident    |
| EventID                | float64   | An identifier for the event                            |
| Latitude               | float64   | The latitude coordinates of the accident location      |
| Longitude              | float64   | The longitude coordinates of the accident location     |
| Make                   | object    | The make of the aircraft involved                      |
| Model                  | object    | The model of the aircraft involved                     |
| AirCraftCategory       | object    | The category of the aircraft                           |
| AirportID              | object    | The identifier for the airport involved (if applicable) |
| AirportName            | object    | The name of the airport (if applicable)                 |
| AmateurBuilt           | object    | Indicates whether the aircraft was amateur-built       |
| NumberOfEngines        | object    | The number of engines on the aircraft                  |
| Scheduled              | object    | Indicates whether the flight was scheduled             |
| PurposeOfFlight        | object    | The purpose of the flight                              |
| FAR                    | object    | A reference to Federal Aviation Regulations            |
| AirCraftDamage         | object    | The extent of damage to the aircraft                   |
| WeatherCondition       | object    | The weather conditions at the time of the accident     |
| Operator               | object    | The operator of the aircraft                            |
| ReportStatus           | object    | The status of the report                                |
| RepGenFlag             | bool      | A report generation flag                                |
| DocketUrl              | object    | A URL associated with the accident report              |
| DocketPublishDate      | object    | The date when the docket was published                  |
