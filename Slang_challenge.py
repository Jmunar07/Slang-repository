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

        # Check if the user has any existing sessions
        if user_id in user_sessions:
            # Check if the current activity is in the same session as the previous activity
            last_session = user_sessions[user_id][-1]
            last_activity_answered_at = last_session["ended_at"]
            if (answered_at - last_activity_answered_at) <= timedelta(minutes=5):
                # Add the current activity to the same session
                last_session["activity_ids"].append(activity_id)
                last_session["ended_at"] = answered_at
                last_session["duration_seconds"] = (answered_at - last_session["started_at"]).total_seconds()
            else:
                # Create a new session for the current activity
                new_session = {
                    "activity_ids": [activity_id],
                    "started_at": first_seen_at,
                    "ended_at": answered_at,
                    "duration_seconds": (answered_at - first_seen_at).total_seconds()
                }
                user_sessions[user_id].append(new_session)
        else:
             # create the first session for the current activity
             new_session = {
                "activity_ids": [activity_id],
                "started_at": first_seen_at,
                "ended_at": answered_at,
                "duration_seconds": (answered_at - first_seen_at).total_seconds()
             }
             user_sessions[user_id] = [new_session]
    

            
    