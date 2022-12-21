# Imported Modules
from pip._vendor import requests
from datetime import datetime, timedelta

# Set up the API
api_endpoint = "https://api.slangapp.com/challenges/v1/activities"
headers = {"Content-Type": "application/json", "Authorization": "Basic MTUyOlVrelczQ2JBaXlaVTNLWTFFVVhPbnhHSTdvaEhpQkVvdURqeEZITHJzUzA9"}

# Fetch data from the API
response = requests.get(api_endpoint, headers=headers)

# Check for success 
if response.status_code == 200:
    print('success')