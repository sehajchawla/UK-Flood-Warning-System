from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
 
stations = build_station_list()
stp10= stations_by_distance(stations, (52.2053, 0.1218))[:10]
stn10= stations_by_distance(stations, (52.2053, 0.1218))[-10:]
"""saving all the stations in two seperate lists"""
for i in range(0,10):
    print((stp10[i][0].name, stp10[i][0].town, stp10[i][1]))

for i in range(0,10):
    print((stn10[i][0].name, stn10[i][0].town, stn10[i][1]))

    
