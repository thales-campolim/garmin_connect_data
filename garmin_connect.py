# garmin_login.py
import os
from dotenv import load_dotenv
from garminconnect import Garmin

# Load environment variables
load_dotenv()

try:
    email = os.environ["GARMIN_EMAIL"]
    password = os.environ["GARMIN_PASSWORD"]
    token_store = os.getenv("GARMIN_TOKENS", "~/.garmin-tokens")
except KeyError as e:
    raise SystemExit(f"Missing required environment variable: {e}")

def garmin_login():
    try:
        # Attempt token-based login first
        client = Garmin()
        client.login(token_store)
        return client
    except Exception:
        # Fallback to email/password with MFA handling
        client = Garmin(email, password)
        client.login()
        
        # Save tokens for future sessions
        client.session.dump(token_store)
        return client

if __name__ == "__main__":
    api = garmin_login()
    print(f"Logged in as: {api.get_full_name()}")
