"""
============================================================================
Project 2: India Tourist Attractions & Tourism Analytics System
Script: 02_Program/tourism_data_cleaning.py
Purpose: Synthetic raw tourism data generation, cleaning, transformation,
         and dimension derivation for 25,000 tourism analytical records.
============================================================================
"""

import math
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set deterministic seed for reproducible analytical dataset
RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# Define Master States & UTs metadata
STATES_DATA = [
    {"StateName": "Andhra Pradesh", "StateType": "State", "Region": "South India", "Capital": "Amaravati"},
    {"StateName": "Arunachal Pradesh", "StateType": "State", "Region": "Northeast India", "Capital": "Itanagar"},
    {"StateName": "Assam", "StateType": "State", "Region": "Northeast India", "Capital": "Dispur"},
    {"StateName": "Bihar", "StateType": "State", "Region": "East India", "Capital": "Patna"},
    {"StateName": "Chhattisgarh", "StateType": "State", "Region": "Central India", "Capital": "Raipur"},
    {"StateName": "Goa", "StateType": "State", "Region": "West India", "Capital": "Panaji"},
    {"StateName": "Gujarat", "StateType": "State", "Region": "West India", "Capital": "Gandhinagar"},
    {"StateName": "Haryana", "StateType": "State", "Region": "North India", "Capital": "Chandigarh"},
    {"StateName": "Himachal Pradesh", "StateType": "State", "Region": "North India", "Capital": "Shimla"},
    {"StateName": "Jharkhand", "StateType": "State", "Region": "East India", "Capital": "Ranchi"},
    {"StateName": "Karnataka", "StateType": "State", "Region": "South India", "Capital": "Bengaluru"},
    {"StateName": "Kerala", "StateType": "State", "Region": "South India", "Capital": "Thiruvananthapuram"},
    {"StateName": "Madhya Pradesh", "StateType": "State", "Region": "Central India", "Capital": "Bhopal"},
    {"StateName": "Maharashtra", "StateType": "State", "Region": "West India", "Capital": "Mumbai"},
    {"StateName": "Manipur", "StateType": "State", "Region": "Northeast India", "Capital": "Imphal"},
    {"StateName": "Meghalaya", "StateType": "State", "Region": "Northeast India", "Capital": "Shillong"},
    {"StateName": "Mizoram", "StateType": "State", "Region": "Northeast India", "Capital": "Aizawl"},
    {"StateName": "Nagaland", "StateType": "State", "Region": "Northeast India", "Capital": "Kohima"},
    {"StateName": "Odisha", "StateType": "State", "Region": "East India", "Capital": "Bhubaneswar"},
    {"StateName": "Punjab", "StateType": "State", "Region": "North India", "Capital": "Chandigarh"},
    {"StateName": "Rajasthan", "StateType": "State", "Region": "West India", "Capital": "Jaipur"},
    {"StateName": "Sikkim", "StateType": "State", "Region": "Northeast India", "Capital": "Gangtok"},
    {"StateName": "Tamil Nadu", "StateType": "State", "Region": "South India", "Capital": "Chennai"},
    {"StateName": "Telangana", "StateType": "State", "Region": "South India", "Capital": "Hyderabad"},
    {"StateName": "Tripura", "StateType": "State", "Region": "Northeast India", "Capital": "Agartala"},
    {"StateName": "Uttar Pradesh", "StateType": "State", "Region": "North India", "Capital": "Lucknow"},
    {"StateName": "Uttarakhand", "StateType": "State", "Region": "North India", "Capital": "Dehradun"},
    {"StateName": "West Bengal", "StateType": "State", "Region": "East India", "Capital": "Kolkata"},
    {"StateName": "Andaman and Nicobar Islands", "StateType": "Union Territory", "Region": "South India", "Capital": "Port Blair"},
    {"StateName": "Chandigarh", "StateType": "Union Territory", "Region": "North India", "Capital": "Chandigarh"},
    {"StateName": "Dadra and Nagar Haveli and Daman and Diu", "StateType": "Union Territory", "Region": "West India", "Capital": "Daman"},
    {"StateName": "Delhi", "StateType": "Union Territory", "Region": "North India", "Capital": "New Delhi"},
    {"StateName": "Jammu and Kashmir", "StateType": "Union Territory", "Region": "North India", "Capital": "Srinagar"},
    {"StateName": "Ladakh", "StateType": "Union Territory", "Region": "North India", "Capital": "Leh"},
    {"StateName": "Lakshadweep", "StateType": "Union Territory", "Region": "South India", "Capital": "Kavaratti"},
    {"StateName": "Puducherry", "StateType": "Union Territory", "Region": "South India", "Capital": "Puducherry"},
]

# Category Groups & Attraction Types
ATTRACTION_TYPES = [
    {"TypeName": "Beach", "Group": "Nature & Coastal"},
    {"TypeName": "Waterfall", "Group": "Nature & Coastal"},
    {"TypeName": "Hill Station", "Group": "Nature & Hill Stations"},
    {"TypeName": "Fort", "Group": "Cultural & Heritage"},
    {"TypeName": "Palace", "Group": "Cultural & Heritage"},
    {"TypeName": "Temple", "Group": "Religious & Spiritual"},
    {"TypeName": "Church", "Group": "Religious & Spiritual"},
    {"TypeName": "Mosque", "Group": "Religious & Spiritual"},
    {"TypeName": "Museum", "Group": "Cultural & Heritage"},
    {"TypeName": "National Park", "Group": "Wildlife & Eco Tourism"},
    {"TypeName": "Wildlife Sanctuary", "Group": "Wildlife & Eco Tourism"},
    {"TypeName": "Trekking", "Group": "Adventure & Recreation"},
    {"TypeName": "Adventure", "Group": "Adventure & Recreation"},
    {"TypeName": "Heritage Site", "Group": "Cultural & Heritage"},
    {"TypeName": "Lake", "Group": "Nature & Hill Stations"},
    {"TypeName": "Cave", "Group": "Cultural & Heritage"},
    {"TypeName": "Island", "Group": "Nature & Coastal"},
    {"TypeName": "Monument", "Group": "Cultural & Heritage"},
]

# Representative major attractions across India
ATTRACTIONS_SEED = [
    # Uttar Pradesh
    {"Name": "Taj Mahal", "State": "Uttar Pradesh", "City": "Agra", "District": "Agra", "Type": "Monument", "Lat": 27.1751, "Lon": 78.0421, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 250.00, "Season": "Winter"},
    {"Name": "Agra Fort", "State": "Uttar Pradesh", "City": "Agra", "District": "Agra", "Type": "Fort", "Lat": 27.1795, "Lon": 78.0211, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 50.00, "Season": "Winter"},
    {"Name": "Kashi Vishwanath Temple", "State": "Uttar Pradesh", "City": "Varanasi", "District": "Varanasi", "Type": "Temple", "Lat": 25.3109, "Lon": 83.0107, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Fatehpur Sikri", "State": "Uttar Pradesh", "City": "Fatehpur Sikri", "District": "Agra", "Type": "Heritage Site", "Lat": 27.0945, "Lon": 77.6679, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 50.00, "Season": "Winter"},
    
    # Rajasthan
    {"Name": "Amer Fort", "State": "Rajasthan", "City": "Jaipur", "District": "Jaipur", "Type": "Fort", "Lat": 26.9855, "Lon": 75.8513, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 100.00, "Season": "Winter"},
    {"Name": "Hawa Mahal", "State": "Rajasthan", "City": "Jaipur", "District": "Jaipur", "Type": "Palace", "Lat": 26.9239, "Lon": 75.8267, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 50.00, "Season": "Winter"},
    {"Name": "Mehrangarh Fort", "State": "Rajasthan", "City": "Jodhpur", "District": "Jodhpur", "Type": "Fort", "Lat": 26.2978, "Lon": 73.0185, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 100.00, "Season": "Winter"},
    {"Name": "City Palace Udaipur", "State": "Rajasthan", "City": "Udaipur", "District": "Udaipur", "Type": "Palace", "Lat": 24.5764, "Lon": 73.6835, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 300.00, "Season": "Winter"},
    {"Name": "Jaisalmer Fort", "State": "Rajasthan", "City": "Jaisalmer", "District": "Jaisalmer", "Type": "Fort", "Lat": 26.9124, "Lon": 70.9126, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 100.00, "Season": "Winter"},
    
    # Maharashtra
    {"Name": "Gateway of India", "State": "Maharashtra", "City": "Mumbai", "District": "Mumbai City", "Type": "Monument", "Lat": 18.9220, "Lon": 72.8347, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Ajanta Caves", "State": "Maharashtra", "City": "Aurangabad", "District": "Chhatrapati Sambhajinagar", "Type": "Cave", "Lat": 20.5519, "Lon": 75.7033, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Ellora Caves", "State": "Maharashtra", "City": "Aurangabad", "District": "Chhatrapati Sambhajinagar", "Type": "Cave", "Lat": 20.0268, "Lon": 75.1780, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Chhatrapati Shivaji Maharaj Terminus", "State": "Maharashtra", "City": "Mumbai", "District": "Mumbai City", "Type": "Heritage Site", "Lat": 18.9400, "Lon": 72.8353, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 0.00, "Season": "All Year"},
    
    # Delhi
    {"Name": "Qutub Minar", "State": "Delhi", "City": "New Delhi", "District": "South Delhi", "Type": "Monument", "Lat": 28.5245, "Lon": 77.1855, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Red Fort", "State": "Delhi", "City": "Old Delhi", "District": "Central Delhi", "Type": "Fort", "Lat": 28.6562, "Lon": 77.2410, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 50.00, "Season": "Winter"},
    {"Name": "Humayun Tomb", "State": "Delhi", "City": "New Delhi", "District": "South Delhi", "Type": "Monument", "Lat": 28.5849, "Lon": 77.2507, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Lotus Temple", "State": "Delhi", "City": "New Delhi", "District": "South Delhi", "Type": "Heritage Site", "Lat": 28.5535, "Lon": 77.2588, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 0.00, "Season": "All Year"},
    
    # Goa
    {"Name": "Calangute Beach", "State": "Goa", "City": "Panaji", "District": "North Goa", "Type": "Beach", "Lat": 15.5494, "Lon": 73.7535, "UNESCO": "Non-UNESCO", "Hist": "Low", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Baga Beach", "State": "Goa", "City": "Panaji", "District": "North Goa", "Type": "Beach", "Lat": 15.5553, "Lon": 73.7517, "UNESCO": "Non-UNESCO", "Hist": "Low", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Basilica of Bom Jesus", "State": "Goa", "City": "Old Goa", "District": "North Goa", "Type": "Church", "Lat": 15.5009, "Lon": 73.9116, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Dudhsagar Falls", "State": "Goa", "City": "Sanguem", "District": "South Goa", "Type": "Waterfall", "Lat": 15.3144, "Lon": 74.3143, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 50.00, "Season": "Monsoon"},
    
    # Kerala
    {"Name": "Munnar Tea Gardens", "State": "Kerala", "City": "Munnar", "District": "Idukki", "Type": "Hill Station", "Lat": 10.0889, "Lon": 77.0595, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Alleppey Backwaters", "State": "Kerala", "City": "Alappuzha", "District": "Alappuzha", "Type": "Lake", "Lat": 9.4981, "Lon": 76.3388, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 500.00, "Season": "Winter"},
    {"Name": "Periyar Wildlife Sanctuary", "State": "Kerala", "City": "Thekkady", "District": "Idukki", "Type": "Wildlife Sanctuary", "Lat": 9.4679, "Lon": 77.1417, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 150.00, "Season": "Winter"},
    
    # Karnataka
    {"Name": "Mysore Palace", "State": "Karnataka", "City": "Mysuru", "District": "Mysuru", "Type": "Palace", "Lat": 12.3052, "Lon": 76.6552, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 100.00, "Season": "Winter"},
    {"Name": "Hampi Monuments", "State": "Karnataka", "City": "Hampi", "District": "Vijayanagara", "Type": "Heritage Site", "Lat": 15.3350, "Lon": 76.4600, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Jog Falls", "State": "Karnataka", "City": "Sagara", "District": "Shivamogga", "Type": "Waterfall", "Lat": 14.2260, "Lon": 74.8118, "UNESCO": "Non-UNESCO", "Hist": "Low", "Fee": 20.00, "Season": "Monsoon"},
    
    # Tamil Nadu
    {"Name": "Meenakshi Amman Temple", "State": "Tamil Nadu", "City": "Madurai", "District": "Madurai", "Type": "Temple", "Lat": 9.9195, "Lon": 78.1193, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Brihadisvara Temple Tanjore", "State": "Tamil Nadu", "City": "Thanjavur", "District": "Thanjavur", "Type": "Temple", "Lat": 10.7828, "Lon": 79.1318, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Shore Temple Mamallapuram", "State": "Tamil Nadu", "City": "Mahabalipuram", "District": "Chengalpattu", "Type": "Heritage Site", "Lat": 12.6169, "Lon": 80.1994, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    
    # Punjab
    {"Name": "Golden Temple", "State": "Punjab", "City": "Amritsar", "District": "Amritsar", "Type": "Temple", "Lat": 31.6200, "Lon": 74.8765, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Wagah Border", "State": "Punjab", "City": "Amritsar", "District": "Amritsar", "Type": "Monument", "Lat": 31.6042, "Lon": 74.5731, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},
    
    # West Bengal
    {"Name": "Victoria Memorial", "State": "West Bengal", "City": "Kolkata", "District": "Kolkata", "Type": "Museum", "Lat": 22.5448, "Lon": 88.3426, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 50.00, "Season": "Winter"},
    {"Name": "Sundarbans National Park", "State": "West Bengal", "City": "Canning", "District": "South 24 Parganas", "Type": "National Park", "Lat": 21.9497, "Lon": 88.9007, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 100.00, "Season": "Winter"},
    {"Name": "Darjeeling Toy Railway", "State": "West Bengal", "City": "Darjeeling", "District": "Darjeeling", "Type": "Heritage Site", "Lat": 27.0410, "Lon": 88.2663, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 500.00, "Season": "Spring"},
    
    # Himachal Pradesh
    {"Name": "Rohtang Pass", "State": "Himachal Pradesh", "City": "Manali", "District": "Kullu", "Type": "Adventure", "Lat": 32.3716, "Lon": 77.2466, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 500.00, "Season": "Summer"},
    {"Name": "Mall Road Shimla", "State": "Himachal Pradesh", "City": "Shimla", "District": "Shimla", "Type": "Hill Station", "Lat": 31.1048, "Lon": 77.1734, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 0.00, "Season": "Summer"},
    
    # Uttarakhand
    {"Name": "Kedarnath Temple", "State": "Uttarakhand", "City": "Kedarnath", "District": "Rudraprayag", "Type": "Temple", "Lat": 30.7352, "Lon": 79.0669, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Summer"},
    {"Name": "Jim Corbett National Park", "State": "Uttarakhand", "City": "Ramnagar", "District": "Nainital", "Type": "National Park", "Lat": 29.5300, "Lon": 78.7747, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 200.00, "Season": "Winter"},

    # Assam
    {"Name": "Kaziranga National Park", "State": "Assam", "City": "Golaghat", "District": "Golaghat", "Type": "National Park", "Lat": 26.5775, "Lon": 93.1711, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 100.00, "Season": "Winter"},
    {"Name": "Kamakhya Temple", "State": "Assam", "City": "Guwahati", "District": "Kamrup Metropolitan", "Type": "Temple", "Lat": 26.1664, "Lon": 91.7061, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},

    # Ladakh
    {"Name": "Pangong Tso Lake", "State": "Ladakh", "City": "Leh", "District": "Leh", "Type": "Lake", "Lat": 33.7595, "Lon": 78.6674, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 0.00, "Season": "Summer"},
    {"Name": "Nubra Valley", "State": "Ladakh", "City": "Diskit", "District": "Leh", "Type": "Adventure", "Lat": 34.5458, "Lon": 77.5673, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 20.00, "Season": "Summer"},

    # Gujarat
    {"Name": "Statue of Unity", "State": "Gujarat", "City": "Kevadia", "District": "Narmada", "Type": "Monument", "Lat": 21.8380, "Lon": 73.7191, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 150.00, "Season": "Winter"},
    {"Name": "Rann of Kutch", "State": "Gujarat", "City": "Bhuj", "District": "Kutch", "Type": "Adventure", "Lat": 23.7337, "Lon": 69.8597, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 100.00, "Season": "Winter"},

    # Odisha
    {"Name": "Konark Sun Temple", "State": "Odisha", "City": "Konark", "District": "Puri", "Type": "Heritage Site", "Lat": 19.8876, "Lon": 86.0945, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Jagannath Temple Puri", "State": "Odisha", "City": "Puri", "District": "Puri", "Type": "Temple", "Lat": 19.8135, "Lon": 85.8312, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 0.00, "Season": "Winter"},

    # Madhya Pradesh
    {"Name": "Khajuraho Group of Monuments", "State": "Madhya Pradesh", "City": "Khajuraho", "District": "Chhatarpur", "Type": "Heritage Site", "Lat": 24.8318, "Lon": 79.9199, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},
    {"Name": "Sanchi Stupa", "State": "Madhya Pradesh", "City": "Sanchi", "District": "Raisen", "Type": "Monument", "Lat": 23.4793, "Lon": 77.7397, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 40.00, "Season": "Winter"},

    # Jammu and Kashmir
    {"Name": "Dal Lake", "State": "Jammu and Kashmir", "City": "Srinagar", "District": "Srinagar", "Type": "Lake", "Lat": 34.1128, "Lon": 74.8731, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 0.00, "Season": "Summer"},
    {"Name": "Gulmarg Ski Resort", "State": "Jammu and Kashmir", "City": "Gulmarg", "District": "Baramulla", "Type": "Adventure", "Lat": 34.0484, "Lon": 74.3805, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 750.00, "Season": "Winter"},

    # Bihar
    {"Name": "Mahabodhi Temple Complex", "State": "Bihar", "City": "Bodh Gaya", "District": "Gaya", "Type": "Temple", "Lat": 24.6960, "Lon": 84.9914, "UNESCO": "UNESCO World Heritage", "Hist": "High", "Fee": 0.00, "Season": "Winter"},

    # Telangana
    {"Name": "Charminar", "State": "Telangana", "City": "Hyderabad", "District": "Hyderabad", "Type": "Monument", "Lat": 17.3616, "Lon": 78.4747, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 25.00, "Season": "Winter"},

    # Meghalaya
    {"Name": "Nohkalikai Falls", "State": "Meghalaya", "City": "Cherrapunji", "District": "East Khasi Hills", "Type": "Waterfall", "Lat": 25.2757, "Lon": 91.6853, "UNESCO": "Non-UNESCO", "Hist": "Moderate", "Fee": 20.00, "Season": "Monsoon"},

    # Sikkim
    {"Name": "Nathula Pass", "State": "Sikkim", "City": "Gangtok", "District": "East Sikkim", "Type": "Trekking", "Lat": 27.3866, "Lon": 88.8309, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 200.00, "Season": "Spring"},

    # Andaman and Nicobar Islands
    {"Name": "Radhanagar Beach", "State": "Andaman and Nicobar Islands", "City": "Havelock Island", "District": "South Andaman", "Type": "Beach", "Lat": 11.9841, "Lon": 92.9507, "UNESCO": "Non-UNESCO", "Hist": "Low", "Fee": 0.00, "Season": "Winter"},
    {"Name": "Cellular Jail", "State": "Andaman and Nicobar Islands", "City": "Port Blair", "District": "South Andaman", "Type": "Museum", "Lat": 11.6739, "Lon": 92.7478, "UNESCO": "Non-UNESCO", "Hist": "High", "Fee": 30.00, "Season": "Winter"},

    # Puducherry
    {"Name": "Promenade Beach", "State": "Puducherry", "City": "Puducherry", "District": "Puducherry", "Type": "Beach", "Lat": 11.9338, "Lon": 79.8353, "UNESCO": "Non-UNESCO", "Hist": "Low", "Fee": 0.00, "Season": "Winter"},
]


def expand_attractions_to_all_states():
    """Generates ~200 diverse attraction records covering all 36 Indian States & UTs."""
    attractions = list(ATTRACTIONS_SEED)
    state_names = [s["StateName"] for s in STATES_DATA]
    covered_states = {a["State"] for a in attractions}
    missing_states = [s for s in state_names if s not in covered_states]

    type_names = [t["TypeName"] for t in ATTRACTION_TYPES]

    for st_name in missing_states:
        st_info = next(s for s in STATES_DATA if s["StateName"] == st_name)
        cap = st_info["Capital"]
        
        # Add 3 attractions per missing state/UT
        for i in range(1, 4):
            atype = random.choice(type_names)
            fee = float(random.choice([0, 20, 50, 100, 200]))
            unesco = "UNESCO World Heritage" if (random.random() < 0.1) else "Non-UNESCO"
            lat = round(random.uniform(8.5, 35.0), 4)
            lon = round(random.uniform(69.0, 95.0), 4)
            
            attractions.append({
                "Name": f"{st_name} {atype} Landmark {i}",
                "State": st_name,
                "City": cap,
                "District": cap,
                "Type": atype,
                "Lat": lat,
                "Lon": lon,
                "UNESCO": unesco,
                "Hist": random.choice(["High", "Moderate", "Low"]),
                "Fee": fee,
                "Season": random.choice(["Winter", "Spring", "Summer", "Monsoon"])
            })
            
    return attractions


def generate_and_clean_tourism_data():
    """
    Generates, cleans, transforms and returns complete normalized DataFrames:
    - df_states (DimStates)
    - df_cities (DimCities)
    - df_types (DimAttractionTypes)
    - df_attractions (DimAttractions)
    - df_dates (DimDates)
    - df_segments (DimVisitorSegments)
    - df_facts (FactTourismVisits: exactly 25,000 records)
    """
    print("Generating and cleaning Tourism dataset (~25,000 records)...")

    # 1. DimStates
    df_states = pd.DataFrame(STATES_DATA)
    df_states["StateID"] = range(1, len(df_states) + 1)
    state_name_to_id = dict(zip(df_states["StateName"], df_states["StateID"]))

    # 2. DimAttractionTypes
    df_types = pd.DataFrame([
        {"AttractionTypeID": i + 1, "AttractionTypeName": t["TypeName"], "CategoryGroup": t["Group"]}
        for i, t in enumerate(ATTRACTION_TYPES)
    ])
    type_name_to_id = dict(zip(df_types["AttractionTypeName"], df_types["AttractionTypeID"]))

    # 3. Master Attractions Data
    raw_attractions = expand_attractions_to_all_states()

    # Extract unique cities
    cities_dict = {}
    city_list = []
    city_id_counter = 1

    for a in raw_attractions:
        key = (a["City"], a["State"])
        if key not in cities_dict:
            st_id = state_name_to_id[a["State"]]
            cities_dict[key] = city_id_counter
            city_list.append({
                "CityID": city_id_counter,
                "CityName": a["City"],
                "StateID": st_id,
                "District": a["District"],
                "Latitude": a["Lat"],
                "Longitude": a["Lon"]
            })
            city_id_counter += 1

    df_cities = pd.DataFrame(city_list)

    # 4. DimAttractions
    attraction_list = []
    for i, a in enumerate(raw_attractions):
        city_id = cities_dict[(a["City"], a["State"])]
        type_id = type_name_to_id[a["Type"]]
        attraction_list.append({
            "AttractionID": i + 1,
            "AttractionName": a["Name"],
            "CityID": city_id,
            "AttractionTypeID": type_id,
            "Description": f"Premier tourist destination located in {a['City']}, {a['State']} featuring exceptional {a['Type'].lower()} experiences.",
            "UNESCOStatus": a["UNESCO"],
            "HistoricalImportance": a["Hist"],
            "BestSeason": a["Season"],
            "EntryFee": float(a["Fee"]),
            "OpeningTime": "08:00 AM" if a["Fee"] > 0 else "06:00 AM",
            "ClosingTime": "06:00 PM" if a["Fee"] > 0 else "08:00 PM"
        })
    df_attractions = pd.DataFrame(attraction_list)

    # 5. DimDates (Monthly records across 2022 - 2025)
    dates_list = []
    seasons_map = {
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Summer",
        6: "Summer", 7: "Monsoon", 8: "Monsoon", 9: "Monsoon",
        10: "Autumn", 11: "Winter"
    }

    date_keys = []
    for yr in [2022, 2023, 2024, 2025]:
        for mo in range(1, 13):
            dt = datetime(yr, mo, 15)
            dt_key = int(dt.strftime("%Y%m%d"))
            date_keys.append(dt_key)
            dates_list.append({
                "DateKey": dt_key,
                "FullDate": dt.strftime("%Y-%m-%d"),
                "Year": yr,
                "Quarter": (mo - 1) // 3 + 1,
                "Month": mo,
                "MonthName": dt.strftime("%B"),
                "Season": seasons_map[mo],
                "Day": 15,
                "IsWeekend": 1 if dt.weekday() in [5, 6] else 0
            })
    df_dates = pd.DataFrame(dates_list)

    # 6. DimVisitorSegments
    segments = ["Domestic", "International", "Family", "Solo", "Couple", "Group"]
    df_segments = pd.DataFrame([
        {"VisitorSegmentID": i + 1, "SegmentName": s} for i, s in enumerate(segments)
    ])

    # 7. FactTourismVisits (Generate EXACTLY 25,000 Records)
    TARGET_RECORDS = 25000
    fact_rows = []

    print(f"Synthesizing {TARGET_RECORDS} analytical observation records...")

    # Pre-map lookup dictionaries for speed
    attraction_city_map = dict(zip(df_attractions["AttractionID"], df_attractions["CityID"]))
    city_state_map = dict(zip(df_cities["CityID"], df_cities["StateID"]))
    attraction_type_map = dict(zip(df_attractions["AttractionID"], df_attractions["AttractionTypeID"]))
    attraction_unesco_map = dict(zip(df_attractions["AttractionID"], df_attractions["UNESCOStatus"]))
    attraction_fee_map = dict(zip(df_attractions["AttractionID"], df_attractions["EntryFee"]))
    attraction_season_map = dict(zip(df_attractions["AttractionID"], df_attractions["BestSeason"]))

    num_attractions = len(df_attractions)
    num_dates = len(df_dates)
    num_segments = len(df_segments)

    for visit_id in range(1, TARGET_RECORDS + 1):
        # Sample dimension FKs
        attr_id = (visit_id % num_attractions) + 1
        date_key = date_keys[(visit_id + visit_id // num_attractions) % num_dates]
        seg_id = ((visit_id * 7) % num_segments) + 1

        city_id = attraction_city_map[attr_id]
        state_id = city_state_map[city_id]
        unesco = attraction_unesco_map[attr_id]
        entry_fee = attraction_fee_map[attr_id]
        best_season = attraction_season_map[attr_id]

        # Extract month/season from date_key
        mo = (date_key // 100) % 100
        curr_season = seasons_map.get(mo, "Winter")

        is_peak = 1 if curr_season == best_season or mo in [10, 11, 12, 1] else 0

        # Base visitor count generation
        base_visitors = int(np.random.normal(loc=18000, scale=6000))
        if unesco == "UNESCO World Heritage":
            base_visitors = int(base_visitors * 1.8)
        if is_peak:
            base_visitors = int(base_visitors * 1.4)
        
        visitor_count = max(800, min(85000, base_visitors))

        # Domestic vs International visitor split
        if unesco == "UNESCO World Heritage" or seg_id == 2:
            intl_pct = random.uniform(0.18, 0.40)
        else:
            intl_pct = random.uniform(0.02, 0.12)

        intl_visitors = int(visitor_count * intl_pct)
        dom_visitors = visitor_count - intl_visitors

        # Rating generation (between 3.20 and 5.00)
        base_rating = 4.3 if unesco == "UNESCO World Heritage" else 3.9
        avg_rating = round(min(5.00, max(3.20, np.random.normal(base_rating, 0.35))), 2)

        # Stay duration (days)
        stay_duration = round(random.uniform(0.5, 4.5), 2)

        # Estimated Revenue (Entry Fee Revenue + Economic Tourism Multiplier)
        ticket_revenue = visitor_count * entry_fee
        economic_spillover = visitor_count * stay_duration * random.uniform(150.0, 450.0)
        est_revenue = round(ticket_revenue + economic_spillover, 2)

        # Popularity score index (0 to 100)
        pop_score = round(min(100.0, max(10.0, (visitor_count / 85000.0 * 50.0) + (avg_rating / 5.0 * 30.0) + (intl_visitors / 25000.0 * 20.0))), 2)

        fact_rows.append({
            "TourismVisitID": visit_id,
            "AttractionID": attr_id,
            "StateID": state_id,
            "CityID": city_id,
            "DateKey": date_key,
            "VisitorSegmentID": seg_id,
            "VisitorCount": visitor_count,
            "DomesticVisitors": dom_visitors,
            "InternationalVisitors": intl_visitors,
            "AverageRating": avg_rating,
            "EntryFee": entry_fee,
            "EstimatedRevenue": est_revenue,
            "PopularityScore": pop_score,
            "AverageStayDuration": stay_duration,
            "IsPeakSeason": is_peak
        })

    df_facts = pd.DataFrame(fact_rows)

    print("Data generation complete.")
    print(f"Dimensions: {len(df_states)} States, {len(df_cities)} Cities, {len(df_types)} Attraction Types, {len(df_attractions)} Attractions, {len(df_dates)} Dates, {len(df_segments)} Visitor Segments.")
    print(f"Fact Table: {len(df_facts)} records cleanly processed.")

    return df_states, df_cities, df_types, df_attractions, df_dates, df_segments, df_facts


if __name__ == "__main__":
    df_st, df_ci, df_ty, df_at, df_da, df_se, df_fa = generate_and_clean_tourism_data()
    print("Sample Fact Row:")
    print(df_fa.head(2))
