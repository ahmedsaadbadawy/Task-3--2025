
                                                                      #Air Traffic Control Sorting Problem


# We will use the Merge Sort algorithm to solve this problem because of its efficiency in handling large datasets. 
# With a time complexity of O(n log n), it is well-suited for air traffic control systems that need to manage hundreds of flights simultaneously.

# Why Merge Sort?
# High Efficiency: It consistently operates in O(n log n) time complexity, making it suitable for sorting large numbers of flights.
# Stable Sorting: It maintains the relative order of flights with the same time value, which is crucial for prioritization.
# Reliable for Large Data: Even though it uses extra memory, it ensures accurate and predictable sorting, which is essential in aviation systems.

class Flight:
    def __init__(self, flight_id, time, altitude, speed):
        self.flight_id = flight_id
        self.time = time
        self.altitude = altitude
        self.speed = speed

    def __str__(self):
        return f"FlightID: {self.flight_id}, Time: {self.time}, Altitude: {self.altitude}, Speed: {self.speed}"

# Merge function to combine sorted halves
def merge(flights, left, mid, right):
    left_part = flights[left:mid + 1]
    right_part = flights[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len(left_part) and j < len(right_part):
        if left_part[i].time <= right_part[j].time:
            flights[k] = left_part[i]
            i += 1
        else:
            flights[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        flights[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        flights[k] = right_part[j]
        j += 1
        k += 1

# Recursive Merge Sort
def merge_sort(flights, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(flights, left, mid)
        merge_sort(flights, mid + 1, right)
        merge(flights, left, mid, right)


if __name__ == "__main__":
  # Sample flight data
    flights = [
        Flight("AA101", 900, 35000, 560),
        Flight("BA202", 730, 36000, 590),
        Flight("CA303", 845, 37000, 600),
        Flight("DA404", 715, 32000, 540),
        Flight("EA505", 930, 34000, 570)
    ]

    print("Before Sorting:")
    for flight in flights:
        print(flight)

    merge_sort(flights, 0, len(flights) - 1)

    print("\nAfter Sorting by Time:")
    for flight in flights:
        print(flight)

# Expected Output:

# Before Sorting:
# FlightID: AA101, Time: 900, Altitude: 35000, Speed: 560
# FlightID: BA202, Time: 730, Altitude: 36000, Speed: 590
# FlightID: CA303, Time: 845, Altitude: 37000, Speed: 600
# FlightID: DA404, Time: 715, Altitude: 32000, Speed: 540
# FlightID: EA505, Time: 930, Altitude: 34000, Speed: 570

# After Sorting by Time:
# FlightID: DA404, Time: 715, Altitude: 32000, Speed: 540
# FlightID: BA202, Time: 730, Altitude: 36000, Speed: 590
# FlightID: CA303, Time: 845, Altitude: 37000, Speed: 600
# FlightID: AA101, Time: 900, Altitude: 35000, Speed: 560
# FlightID: EA505, Time: 930, Altitude: 34000, Speed: 570

# Impact on Real-Time Air Traffic Control:
# Improved Scheduling: Helps efficiently order flights based on arrival/departure times, reducing delays.
# Enhanced Safety: Ensures proper sequencing of flights, minimizing risks of mid-air conflicts.
# Scalability: Since Merge Sort is efficient for large datasets, it can work well in high-traffic airspace situations.
