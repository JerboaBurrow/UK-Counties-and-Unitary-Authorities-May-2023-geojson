"""
Process https://geoportal.statistics.gov.uk/datasets/25dcac5ba5d246138968da883bc412df_0/about into
 individual geojson files converting to LatLon and setting ["properties"]["CTYUA23NM"] as ["properties"]["name"]
"""

import json
from pyproj import Proj
from glob import glob

from tqdm import tqdm

from pyproj import Proj

def to_latlng(data):
    p = Proj("EPSG:27700")
    for f in range(len(data["features"])):
        type = data["features"][f]["geometry"]["type"]
        for (i,coord) in enumerate(data["features"][f]["geometry"]["coordinates"]):
            if type == "MultiPolygon":
                for (j, poly) in enumerate(coord):
                    for (k, vertex) in enumerate(poly):
                        data["features"][f]["geometry"]["coordinates"][i][j][k] = p(*vertex, inverse=True)

            else:
                for (j, vertex) in enumerate(coord):
                    data["features"][f]["geometry"]["coordinates"][i][j] = p(*vertex, inverse=True)

data = json.load(open("counties.geojson"))

to_latlng(data)

for fea in tqdm(data["features"]):
    name = fea["properties"]["CTYUA23NM"]
    name = name.replace(" ", "_")
    name = name.replace(".", "")
    fea["properties"]["name"] = name
    with open(f"{name}.geojson", "w") as out:
        print(json.dumps(fea), file=out)