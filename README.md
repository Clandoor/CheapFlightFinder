# CheapFlightFinder
This Project sends real time alerts whenever flights prices are low.

<h2>Getting your Sheety's details</h2>

1. Go to 'sheety.co' and connect your google account (Make sure it's the same account as the one with which you will use Google Sheet with).

2. Once signed up, create a new project by simply pasting the your google sheet's link and give the project an appropriate name.

3. Enable 'Get', 'Post', 'Put' and 'Delete' requests.

4. These are the appropriate datafields (Simply pass them as a part of the API Endpoint).
   
   <b>Make sure to use your own.</b>
   
   Username: 91e06e6e965b0c3132c2950cf40cfaf3
   
   Project Name: flightTicketsData
   
   Sheet Name: sheet1
   <img width="871" alt="image" src="https://github.com/Clandoor/CheapFlightFinder/assets/42005547/ce47912f-59b2-4a0b-b6ea-cf7f360735d8">

<h2>Getting your Flights Details with API</h2>

1. Sign up and Login with in 'tequila.kiwi.com'.

2. Select the Project and go to 'Search' under the 'Tequilia API'.
   <img width="960" alt="image" src="https://github.com/Clandoor/CheapFlightFinder/assets/42005547/e397fc52-215f-4931-87e8-2fa42e994722">

3. Check and edit which parameters you want to pass under this section and which ones are mandatory.

<h1>Set up App Password</h1>
In order to make Python access and login your gmail account and send emails, you need to set up an app password and allow.
Follow this link for more details 'https://support.google.com/mail/answer/185833?hl=en'.

<h1>After getting the necessary details</h1>
Once you have all the necessary details, replace the constants in the .py files with your own details.

Keep a note that only 200 API calls can be made per month with Sheety free version. Be mindful of this while developing.
