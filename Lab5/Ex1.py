# Define a dictionary named taxi_trip_info with the following key value pairs:
# And print the taxi trip info and taxi trip miles.

# Name: Ava Puaatuua
# Date: Sept. 23, 2026

taxi_trip_info = {
    "Trip_id": "da7a62fce",
    "Trip_seconds": 360,
    "Trip_miles": 1.1,
    "Fare": "$6.25"
}

print("Taxi trip information:", taxi_trip_info)
print("Trip miles:", taxi_trip_info.get("Trip_miles"))
# Using get() is safer because it returns 'None' if the key does not exist
# Can also do taxi_trip_info["Trip_miles"] but if the key does not exist, it will raise a KeyError
print("Fare:", taxi_trip_info.get("Fare"))
