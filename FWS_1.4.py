from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_on_rivers
from floodsystem.stationdata import build_station_list

stations = build_station_list()

"""rivers have at least one monitoring station"""
set_of_rivers=rivers_with_station(stations)
list_of_rivers=list(set_of_rivers)

"""prints the first 10 of these rivers in alphabetical order"""
print(sorted(list_of_rivers)[:10])

"""dictionary that maps river names to a list of stations on a given river"""
dictionary_of_rivers=stations_on_rivers(set_of_rivers,stations)

"""print the names of the stations located on some rivers in alphabetical order"""
print(sorted(dictionary_of_rivers['River Aire']))
print(sorted(dictionary_of_rivers['River Cam']))
print(sorted(dictionary_of_rivers['Thames']))

