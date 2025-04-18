import requests

def get_github_user(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    if response.status_code == 200:
        return response.json().get("login")
    return None