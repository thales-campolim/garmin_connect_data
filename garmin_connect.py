import os
import garminconnect
from garth import http
from datetime import date, timedelta


# Set the User-Agent
http.USER_AGENT = {"User-Agent": "GCM-iOS/5.7.2.1"}

# Debug: Print environment variables
print("GARMIN_EMAIL environment variable:", os.getenv("GARMIN_EMAIL"))
print("GARMIN_PASSWORD environment variable:", "***" if os.getenv("GARMIN_PASSWORD") else "Not set")

# Get credentials from environment variables
email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")

# Check if credentials are set
if not email or not password:
    raise ValueError("Environment variables GARMIN_EMAIL and GARMIN_PASSWORD must be set")

# Initialize Garmin client
garmin = garminconnect.Garmin(email, password)

# Attempt login
try:
    garmin.login()
    print("Login successful")
except Exception as e:
    print(f"Login failed: {str(e)}")

# Set token path
GARTH_HOME = os.path.expanduser("~/.garth")
print(f"Token path: {GARTH_HOME}")

# Attempt to save tokens
try:
    garmin.garth.dump(GARTH_HOME)
    print("Tokens saved successfully")
except Exception as e:
    print(f"Failed to save tokens: {str(e)}")

today = date.today()
today = today.isoformat()

lastrun = garmin.get_last_activity()['splitSummaries'][0]
stats = garmin.get_max_metrics(today)

vo2max = stats[0]['generic']['vo2MaxPreciseValue']
miles = round(lastrun['distance']/1609.34, 2)
effect = garmin.get_last_activity()['trainingEffectLabel']
duration = round(garmin.get_last_activity()['duration'], 2)

records = garmin.get_personal_record()