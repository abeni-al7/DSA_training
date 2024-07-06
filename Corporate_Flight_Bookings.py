class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n
        for booking in bookings:
            first, last, seats = booking
            flights[first - 1] += seats
            if last < n:
                flights[last] -= seats
        for i in range(1, n):
            flights[i] += flights[i - 1]
        return flights
        
