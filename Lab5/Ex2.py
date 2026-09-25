# Write Python code to define a list of taxi trip durations in miles (use values 1.1, 0.8, 2.5, 2.6). 
# Also define a tuple of fares for the same number of trips (use values “$6.25,” “$5.25,” “$10.50,” “$8.05”). 
# Store both the tuple and the list as values in a dictionary called trips, with keys “miles” and “fares.” 
# Print out the dictionary to show what it looks like.

# Name: Ava Puaatuua
# Date: Sept. 23, 2026

trip_durations = [1.1, 0.8, 2.5, 2.6] # List
fares = ("$6.25", "$5.25", "$10.50", "$8.05") # Tuple

trips = {
    "miles": trip_durations,
    "fares": fares
}

print(trips)

# Duration and cost of the third trip
# print("Duration and cost of the third trip:", trips["miles"][2], trips["fares"][2])
print("The duration of the 3rd trip is:", trips["miles"][2], " miles")
print("The cost of the 3rd trip is:", trips["fares"][2])
