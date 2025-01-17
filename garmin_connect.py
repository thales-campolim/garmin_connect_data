from dotenv import load_dotenv
import os
from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError
)

load_dotenv()

garmin_username = os.getenv('GARMIN_USERNAME')
garmin_password = os.getenv('GARMIN_PASSWORD')

if not garmin_username or not garmin_password:
    raise ValueError("Garmin username or password not set in environment variables.")

try:
    client = Garmin(garmin_username, garmin_password)
    client.login()
except (
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError
) as err:
    print(f"Error occurred: {err}")

activity_data = client.get_activities("2025-01-01", "2025-01-15")