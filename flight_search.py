import requests
from datetime import date, timedelta
from flight_data import FlightData

KIWI_API_IAA_CODE_ENDPOINT = 'https://api.tequila.kiwi.com/locations/query'
KIWI_API_SEARCH_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'
KIWI_API_KEY = 'gryfKhvGE1iCSEdVE69ev48vrJ3qaGG7'


class FlightSearch:
    """
    This class is responsible for communicating to the Flight Search API.
    """

    def __init__(self, city_name):
        self.city_name = city_name
        self.kiwi_api_header = {
            'apikey': KIWI_API_KEY
        }

    def get_city_iata_code(self, city_name):
        """
        This function is responsible for fetching the IATA Code for the City based on the city name passed.
        :param city_name: The name of the city passed.
        :return: str
        """

        kiwi_api_parameters = {
            'term': city_name
        }
        api_response = requests.get(url=KIWI_API_IAA_CODE_ENDPOINT,
                                    params=kiwi_api_parameters,
                                    headers=self.kiwi_api_header)

        return api_response.json()['locations'][0]['code']

    def search_flights(self, destination_iata_code):
        """

        :return:
        """

        departure_date, date_after_six_months = date.today(), date.today() + timedelta(days=180)
        departure_date = departure_date.strftime("%d/%m/%G")
        date_after_six_months = date_after_six_months.strftime("%d/%m/%G")

        api_parameters = {
            'fly_from': 'YYZ',
            'fly_to': destination_iata_code,
            'date_from': departure_date,
            'date_to': date_after_six_months,
            'curr': 'CAD'
        }

        flight_search_api_response = requests.get(url=KIWI_API_SEARCH_ENDPOINT,
                                                  headers=self.kiwi_api_header,
                                                  params=api_parameters)

        flight_details = flight_search_api_response.json()['data']
        print(flight_details[0]['price'])
        all_flight_data = FlightData(price=flight_details[0]['price'],
                                     departure_city=flight_details['route'][0]['cityFrom'],
                                     departure_airport_code=flight_details['route'][0]['flyFrom'],
                                     arrival_city=flight_details['route'][0]['cityTo'],
                                     arrival_airport_code=flight_details['route'][0]['route']['flyTo'],
                                     departure_date=flight_details['route'][0]['local_departure'].split('T')[0],
                                     date_after_six_months=flight_details['route'][1]['local_departure'].split('T')[0])

        # details = (f"Price: {flight_details[0]['price']} CAD."
        #            f"Departure City: {flight_details[0]['cityFrom']}"
        #            f"Departure Airport Code: {flight_details[0]['flyFrom']}"
        #            f"Arrival City: {flight_details[0]['cityTo']}"
        #            f"Arrival Airport Code: {flight_details[0]['flyTo']}"
        #            f"Departure Date: {flight_details[0]['local_departure'].split('T')}"
        #            f"Arrival Date: {flight_details[0]['local_arrival'].split('T')}")

        return all_flight_data
