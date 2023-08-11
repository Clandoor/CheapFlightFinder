
"""
This is the main driver class which will use different classes to execute the main program.
"""

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

s = DataManager()
sheet_data = s.fetch_prices()
print(sheet_data)

for entry in sheet_data['sheet1']:
    flight = FlightSearch(entry['city'])
    iata_code = flight.get_city_iata_code(entry['city'])

    iata_data = {
        'sheet1': {
            'iataCode': iata_code
        }
    }
    s.populate_iata_field(iata_data, entry['id'])
    all_flight_data = flight.search_flights(iata_code)

    if all_flight_data.price < entry['lowestPrice']:
        message = (f"Subject: Alert!! Low Prices\n\n"
                   f"Only {all_flight_data.price} CAD to fly from {all_flight_data.departure_city}"
                   f"-{all_flight_data.departure_airport_code} to "
                   f"{all_flight_data.arrival_city}-{all_flight_data.arrival_airport_code} "
                   f"from {all_flight_data.departure_date} to {all_flight_data.date_after_six_months}")

        send_email = NotificationManager(message_to_send=message)
