from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations



stations = build_station_list()
"""buiding list of all stations in order to implement the function on it"""

print_list = []
for i in inconsistent_typical_range_stations(stations):
    print_list.append(i.name)
    """prints the list of names in alphabetical order that are inconsistent"""
print(sorted(print_list))

