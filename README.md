## Source
From UK Government, Office for National Statistics https://geoportal.statistics.gov.uk/datasets/25dcac5ba5d246138968da883bc412df_0/about
- Contains OS data © Crown copyright and database right [2024]
- Contains Royal Mail data © Royal Mail copyright and Database right [2024]
- Contains GeoPlace data © Local Government Information House Limited copyright and database right [2024]
- Source: Office for National Statistics licensed under the Open Government Licence v.3.0

## Processing

The original geojson data was transformed using https://github.com/JerboaBurrow/UK-Counties-and-Unitary-Authorities-May-2023-geojson/blob/main/extract_counties.py.

- Converts from ```EPSG:27700``` to LatLon
- Inserts ```["properties"]["CTYUA23NM"]``` as ```["properties"]["name"]```
- Splits into seperate geojson files
