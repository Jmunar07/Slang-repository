# Imported Modules
from pip._vendor import requests
from datetime import datetime, timedelta

# Set up the API
api_endpoint = "https://api.slangapp.com/challenges/v1/activities"
headers = {"Content-Type": "application/json", "Authorization": "Basic MTUyOlVrelczQ2JBaXlaVTNLWTFFVVhPbnhHSTdvaEhpQkVvdURqeEZITHJzUzA9"}

# Fetch data from the API
response = requests.get(api_endpoint, headers=headers)

# Checking success accessing data
if response.status_code == 200:
    # Parse the received json
    data = response.json()
    activities = data["activities"]

    # Create a list of user sessions from the parsed JSON
    user_sessions = {}
    for activity in activities:
        user_id = activity["user_id"]
        activity_id = activity["id"]
        answered_at = datetime.fromisoformat(activity["answered_at"])
        first_seen_at = datetime.fromisoformat(activity["first_seen_at"])
    
    