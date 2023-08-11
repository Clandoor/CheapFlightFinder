import requests

USERNAME = '91e06e6e965b0c3132c2950cf40cfaf3'
PROJECT_NAME = 'flightTicketsData'
SHEET_NAME = 'sheet1'
SHEETY_API_ENDPOINT = f'https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}'


class DataManager:
    """
    This class is responsible for communicating to the Google Sheet.
    """

    def __init__(self):
        self.api_header = {
            'Authorization': 'Bearer this_is_a_secret_token'
        }

        self.sheety_get_response = requests.get(url=SHEETY_API_ENDPOINT, headers=self.api_header)

    def fetch_prices(self):
        """
        This function fetches the details from the .json file and returns it.
        :return: List
        """

        return self.sheety_get_response.json()

    def populate_iata_field(self, data, row_index):
        """
        This function fills out the IATA field in the Google Sheets.
        :return: None
        """

        api_put_response = requests.put(url=f'{SHEETY_API_ENDPOINT}/{row_index}',
                                        headers=self.api_header,
                                        json=data)
