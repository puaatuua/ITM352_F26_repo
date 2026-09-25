# Use the zip() function to create a dictionary where the keys are the durations and the values are the fares
# And print out the duration and cost of the 3rd trip.

# Name: Ava Puaatuua
# Date: Sept. 23, 2026

trip_durations = [1.1, 0.8, 2.5, 2.6] # List
fares = ("$6.25", "$5.25", "$10.50", "$8.05") # Tuple

trips = dict(zip(trip_durations, fares))
print(trips)

trip_num = int(input("What trip do you want?"))

print("The duration of the trip is:", trip_durations[trip_num-1], " miles")
print("The fare of the trip is:", fares[trip_num-1])