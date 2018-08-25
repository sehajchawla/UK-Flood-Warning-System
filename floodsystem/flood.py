from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    output_list = []
    stations_that_are_flooding = []
    relative_water_level = []
    for i in stations:
        if i.relative_water_level() != None:
            """adding all things  that are larger than the tolerance level"""
            if i.relative_water_level()> tol:
                stations_that_are_flooding.append(i.name)
                relative_water_level.append(i.relative_water_level())
    for j in range(1,len(stations_that_are_flooding)):
        """putting them in one tuple"""
        output_list.append((stations_that_are_flooding[j],relative_water_level[j]))
    """sorting stuff out, cuz i don't like a mess :D"""
    output_list = sorted_by_key(output_list,1)
    output_list = output_list[::-1]
    return(output_list)
    
def stations_highest_rel_level(stations, N):
    output_list = []
    station_name = []
    relative_water_level = [] 
    for i in stations:
        """Making up a randomish list of all sttaions and relative levels"""
        if i.relative_water_level() != None:    
            station_name.append(i.name)
            relative_water_level.append(i.relative_water_level())
    for j in range(1,len(station_name)):
        """putting them in one tuple"""
        output_list.append((station_name[j],relative_water_level[j]))
    """sorting the stuff out well and good"""
    output_list = sorted_by_key(output_list,1) 
    output_list = output_list[::-1]
    output_list = output_list[0:N]
    return(output_list)
    
        