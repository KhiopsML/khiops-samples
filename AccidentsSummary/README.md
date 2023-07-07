# AccidentsSummary Dataset

Simpler version of the `Accidents` dataset, using a star schema:
- The target value is precomputed in the `Accident` table
- The `Place` and `User` tables are omitted
- The `GPSCode`, `Latitude` and `Longitude` are omitted from the `Accident` table
- Schema:
```
Accident
|
| --- 1-n --- Vehicle
```
