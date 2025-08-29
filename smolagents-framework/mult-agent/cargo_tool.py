# ------------------------------------------
# Beginning to create a tool for multi agent
# simple reference as one might be done
# ------------------------------------------
import math
from typing import Optional, Tuple
from smolagents import tool

@tool
def calculate_cargo_time(
        og_coords: Tuple[float, float],
        dest_coords: Tuple[float, float],
        plane_speed_kmh: Optional[float] = 750.0,
        ) -> float:
    """
    Calucalte the trave time of a plane between two points on Earth.
    Uses great-circle distance for the calculation.
    
    Args:
    og_coords: Origin Coordinates used as a starting point Tuple of latitude and longitude
    dest_coords: Destination Coordinates used as the end point Tuple of latitued and longitude
    plane_speed_kmh: Optional argument, defining the cruising speed in km/h default to 750 km/h
    
    Returns:
    float: The estimated travel time in hours

    Example:
    Chicago (41.8781 N, 87.6298 W) to Sydney (33.8688 S, 151.2093 E)
    Result = calculate_cargo_time((41.8781, -87.6298), (-33.8688, 151.2093))
    """
    #---------------------------------------
    # Function used later on in calculations
    #---------------------------------------
    def to_radians(degrees: float) -> float:
        return (degrees * (math.pi / 180))
    
    #--------------------
    # Extract coordinates
    #--------------------
    latitude_og, longitude_og = map(to_radians, og_coords)
    latitude_dst, longitude_dst = map(to_radians, dest_coords)

    #-------------------------------------------------
    # Constant value, whole earth radius in kilometers
    #-------------------------------------------------
    EARTH_RAD_KM = 6371.0

    #----------------------------------------------------------------
    # Calculation of great-cirle distance using the haversine formula
    #----------------------------------------------------------------
    distance_long = longitude_dst - longitude_og
    distance_latitude = latitude_dst - latitude_og

