from geopy.distance import geodesic
import math

def haversine(coord1, coord2):
    return geodesic(coord1, coord2).meters

def calculate_heading(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    distance = haversine(coord1, coord2)

    if distance == 0:
        return "forward"

    try:
        angle = 180 * (delta_lon / max(1e-9, abs(delta_lon))) * math.acos(delta_lat / max(1e-9, distance)) / math.pi
    except ValueError:
        return "forward"

    if angle > 0:
        return "right"
    elif angle < 0:
        return "left"
    else:
        return "forward"




def calculate_distance_and_heading(current_coord, next_coord):
    distance = haversine(current_coord, next_coord)
    heading = calculate_heading(current_coord, next_coord)
    return distance, heading

def calculate_actions(coordinates):
    actions = []

    for i in range(1, len(coordinates)):
        current_coord = coordinates[i - 1]
        next_coord = coordinates[i]

        distance, heading = calculate_distance_and_heading(current_coord, next_coord)

        if i == 1:
            actions.append(f"{distance:.2f} meters forward")
        else:
            actions.append(f"{distance:.2f} meters {heading}")

    return actions

custom_coordinates = [
    (5.117893, -1.296080),
    (5.118067, -1.296201),
    (5.118133, -1.296189),
    (5.118272, -1.296147),
    (5.118404, -1.296177),
    (5.118506, -1.296117),
    (5.118548, -1.296123),
    (5.118825, -1.296153),
    (5.118921, -1.296322),
    (5.118927, -1.296485),
    (5.118945, -1.296606),
    (5.119095, -1.296594),
    (5.119402, -1.296612),
    (5.119613, -1.296588),
    (5.119787, -1.296563),
    (5.120527, -1.296412),
    (5.120749, -1.296286),
    (5.120906, -1.296286),
    (5.121098, -1.296292),
    (5.121189, -1.296153),
    (5.121224, -1.296085),
    (5.121309, -1.295976),
    (5.121549, -1.295831),
    (5.121550, -1.295831),
]

actions = calculate_actions(custom_coordinates)

for action in actions:
    print(action)
