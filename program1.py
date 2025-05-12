import random

# Traffic data: number of vehicles at each signal
traffic = {
    'North': random.randint(5, 50),
    'South': random.randint(5, 50),
    'East': random.randint(5, 50),
    'West': random.randint(5, 50)
}

# Function to calculate green light time
def get_green_time(vehicles):
    if vehicles > 40:
        return 30  # seconds
    elif vehicles > 30:
        return 25
    elif vehicles > 20:
        return 20
    else:
        return 15

# Simulate one cycle of traffic signal
for direction in traffic:
    vehicles = traffic[direction]
    green_time = get_green_time(vehicles)
    print(f"{direction} side has {vehicles} vehicles.")
    print(f"Green light ON for {green_time} seconds.\n")