from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()

stations=stations_within_radius(stations,(52.2053, 0.1218),10)
stations_name=[]
for i in stations:
    stations_name.append(i.name)

print(sorted(stations_name))
