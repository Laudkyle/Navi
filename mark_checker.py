from geopy.distance import geodesic

def is_within_area(current_location, area_center, radius_km):
    """
    Check if the current location is within a specified area.

    Parameters:
    - current_location: Tuple of (latitude, longitude) for the current location.
    - area_center: Tuple of (latitude, longitude) for the center of the area.
    - radius_km: Radius of the area in kilometers.

    Returns:
    - True if the current location is within the area, False otherwise.
    """
    current_coordinates = (current_location[0], current_location[1])
    area_coordinates = (area_center[0], area_center[1])

    distance = geodesic(current_coordinates, area_coordinates).kilometers

    return distance <= radius_km

# Example usage:
current_location = (37.7749, -122.4194)  # Replace with your current location
area_center = (37.7749, -122.4194)  # Replace with the center of the area
radius_km = 5  # Replace with the radius of the area in kilometers

result = is_within_area(current_location, area_center, radius_km)

if result:
    print("You are within the specified area.")
else:
    print("You are outside the specified area.")
