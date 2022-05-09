import re

hotels = ['Lakewood', 'Bridgewood', 'Ridgewood']

days_of_week = ['mon', 'tues', 'wed', 'thur', 'fri', 'sat', 'sun']

values_by_hotel = {
    "Lakewood": {
        "midweek": {
            "Regular": 110,
            "Rewards": 80
        },
        "weekend": {
            "Regular": 90,
            "Rewards": 80
        },
        "class": 3
    },
    "Bridgewood": {
        "midweek": {
            "Regular": 160,
            "Rewards": 110
        },
        "weekend": {
            "Regular": 60,
            "Rewards": 50
        },
        "class": 4
    },
    "Ridgewood": {
        "midweek": {
            "Regular": 220,
            "Rewards": 100
        },
        "weekend": {
            "Regular": 150,
            "Rewards": 40
        },
        "class": 5
    }
}

def get_day_of_the_week(txt) -> list:
    days = re.findall(r'\((.*?)\)', txt)
    return days if days else None  

def get_type_client(txt) -> str:
    client = txt.split(":")[0]
    return client if client in ["Regular", "Rewards"] else None

def get_cheapest_hotel(txt) -> str:   #DO NOT change the function's name
    # Get visiting days
    days = get_day_of_the_week(txt)
    client = get_type_client(txt)

    # Check input is in correct format
    if days is None or client is None:
        return None
    
    # Checks total value for each hotel
    hotels_total = { }
    for hotel in hotels:
        total = 0
        for day in days:
            mid_or_end = 'midweek' if days_of_week.index(day) < 5 else 'weekend'
            total += values_by_hotel[hotel][mid_or_end][client]
        
        if len(hotels_total.keys()) == 0:
            hotels_total['hotel'] = hotel
            hotels_total['total'] = total
        
        # Check which hotel has the lowest value
        elif hotels_total['total'] > total:
                hotels_total['hotel'] = hotel
                hotels_total['total'] = total
        
        # If total is equal, check by rank
        elif hotels_total['total'] == total and values_by_hotel[hotel]['class'] > values_by_hotel[hotels_total['hotel']]['class']:
            hotels_total['hotel'] = hotel
            hotels_total['total'] = total
    
    return hotels_total['hotel']