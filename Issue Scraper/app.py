# File: step2_error_handling.py
import requests
import sys

def fetch_repo_info(owner, repo_name):
    """Fetch information about a repository"""
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises exception for bad status codes
        
        data = response.json()
        return {
            'name': data['full_name'],
            'description': data['description'],
            'stars': data['stargazers_count'],
            'open_issues': data['open_issues_count']
        }
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Test it
if __name__ == "__main__":
    info = fetch_repo_info("Ardupilot", "ardupilot")
    if info:
        print(f"✅ Success! Found: {info['name']} with {info['stars']} stars")