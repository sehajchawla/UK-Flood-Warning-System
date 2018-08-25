
"""This module contains a collection of functions related to
geographical data.

"""

"""The first part of this is basically haversine function that allows me 
to calculate the distance between stations and p"""

from math import radians, cos, sin, asin, sqrt
from floodsystem.utils import sorted_by_key

AVG_EARTH_RADIUS = 6371  # in km
MILES_PER_KILOMETER = 0.621371

def haversine(point1, point2, miles=False):
    """ Calculate the great-circle distance between two points on the Earth surface.
    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.
    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))
    :output: Returns the distance between the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.
    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * MILES_PER_KILOMETER # in miles
    else:
        return h  # in kilometers

"""This is where the rest of it starts"""


def stations_by_distance(stations, p):
    output_list = []
    for i in stations:
        """Iterates through the list named "stations" given to the function"""
        dist= haversine(p,i.coord)
        output_list.append((i,dist))
    output_list = sorted_by_key(output_list,1)
    """This uses the function from the utils file and outputs the same list, 
    but sorted based on the 2nd element which has i=1"""
    return(output_list)
  
"""Task 1C-Find the stations that are within distance r from the centre"""
def stations_within_radius(stations, centre, r):
    """Call the function from task 1B to find the distance of the stations from the centre"""
    station_distance=stations_by_distance(stations,centre)
    stations_within_r=[]
    """Iterate through the the list of distances to find the ones that are less than r"""
    for i in station_distance:
        if i[1]<r:
            stations_within_r.append(i[0])
    return stations_within_r

"""Task 1D- the set of rivers"""
def rivers_with_station(stations):
    rivers=set()
    """iterate through the stations and add the corresponding river to the set"""
    for i in stations:
        rivers=rivers^set([i.river])
    return rivers

"""Task 1D- a dictionary that maps the stations to the rivers"""
def stations_on_rivers(rivers,stations):
    output_dict={}
    """create a dictionary with river names as the keys and empty lists as thevalues"""
    for i in rivers:
        output_dict[i]=[]
    """Add the station names to the lists of the corresponding rivers"""
    for i in stations:
        if i.river in rivers:
            output_dict[i.river].append(i.name)
    return output_dict
    

    
def rivers_by_station_number(stations, N):
    output_list = []
    rivers =[]
    number_of_rivers=[]
    for i in stations:
        """Iterates through stations that are given to the function"""
        if i.river not in rivers:
            """Adds a new entry to rivers when new river is seen and 
            initializes that rivers number to 1"""
            rivers.append(i.river)
            number_of_rivers.append(1)
        else:
            """Keeps adding 1 to every river that is already in the list"""
            for j in range(0,len(rivers)):
                if rivers[j]==i.river:
                    number_of_rivers[j]= number_of_rivers[j] + 1
    for w in range(0, len(rivers)):
        """combines the rivers and number of rivers list into one as tuples"""
        output_list.append((rivers[w],number_of_rivers[w]))
    """sorts them based on the number of rivers"""
    output_list = sorted_by_key(output_list,1)
    """orders it from highest to lowest"""
    output_list = output_list[::-1]
    while output_list[N-1][1]==output_list[N][1]: 
        """Checks if the next few rivers also have the same number and 
        outputs them if they do"""
        N=N+1
    return(output_list[:N]) 
    
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        