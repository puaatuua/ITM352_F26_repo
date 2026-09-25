# Modify the code from Ex2d.py to use numbers instead of strings for the fares.

# Name: Ava Puaatuua
# Date: Sept. 23, 2026

trip_durations = [1.1, 0.8, 2.5, 2.6] # List
fares = (6.25, 5.25, 10.50, 8.05) # Tuple

trips = [
    {"duration": 1.1, "fare": 6.25},
    {"duration": 0.8, "fare": 5.25},
    {"duration": 2.5, "fare": 10.50},
    {"duration": 2.6, "fare": 8.05}
]

print(trips)
print("The duration of the 3rd trip is:", trips[2]["duration"], " miles")
print("The fare of the 3rd trip is:", trips[2]["fare"])