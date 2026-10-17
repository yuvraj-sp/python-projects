import requests
from twilio.rest import Client

OWM_endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="43db88fdd4aa2444103a6f31dddd14ec"
account_sid = "AC1eb1fe5708bf6c61b85915a586c00490"
auth_token = "77b034d66b557557d42827e1d3bdd98c"


weather_parameter = {
    "lat":28.704060,
    "lon":77.102493,
    "appid":api_key,
    "cnt":4
}

response = requests.get(OWM_endpoint,params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
# print(response.json())
# print(data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

# index based loop
# for i in range(0,4):
#     condition_code = data["list"][i]["weather"][0]["id"]
#     i=i+1
#     if int(condition_code) < 700:
#         will_rain=True

if will_rain:
    # print("Bring Umbrella")
    
    client = Client(account_sid,auth_token)
# _______________ method to sent SMS____________________
    # message=client.messages \
    #     .create(
    #         body="It's going to rain today.Remember to bring an ☂️",
    #         from_="+16506743338",
    #         to="+917822961644"
    # )
# ________________Method for Whatsapp Message______________
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+917822961644"
    )
    print(message.status)   #shows the status of message
