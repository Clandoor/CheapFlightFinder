
class FlightData:
    """
    This class is responsible for structuring the flight data.
    """

    def __init__(self, price, departure_city, departure_airport_code, arrival_city,
                 arrival_airport_code, departure_date, date_after_six_months):

        self.price = price
        self.departure_city = departure_city
        self.departure_airport_code = departure_airport_code,
        self.arrival_city = arrival_city,
        self.arrival_airport_code = arrival_airport_code,
        self.departure_date = departure_date
        self.date_after_six_months = date_after_six_months
