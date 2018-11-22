data = {"dry": {"low": 5, "medium":7.5, "hot": 9.5}, "moist": {"low": 4.5, "medium":6.5, "hot": 8.5}, "wet": {"low": 3.5, "medium":5.5, "hot": 6.5}}

def water_requirement(soil_type, temp):
    return data[soil_type][temp]