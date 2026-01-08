# File: step1_basic.py
import requests  # Library for making HTTP requests

# GitHub API endpoint for a specific repository
url = "https://api.github.com/repos/ArduPilot/ardupilot"

# Make the request
response = requests.get(url)
print(response.content)
# Check if successful
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dictionary
    print(f"Repository: {data['full_name']}")
    print(f"Description: {data['description']}")
    print(f"Stars: {data['stargazers_count']}")
else:
    print(f"Error: {response.status_code}")