from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level


"""just bringing everything together and printing the stuff"""

stations = build_station_list()
update_water_levels(stations)

print(stations_highest_rel_level(stations, 10))