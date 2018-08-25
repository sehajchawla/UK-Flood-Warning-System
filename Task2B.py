from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

"""just bringing everything together and printing the stuff"""

stations = build_station_list()
update_water_levels(stations)
print(stations_level_over_threshold(stations, 0.8))