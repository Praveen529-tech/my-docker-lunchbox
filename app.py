import requests,math

def check_github_status():
    response = requests.get("https://api.github.com", timeout=5)
    return response.status_code

def get_greeting():
    status = check_github_status()
    return f"Hello! GitHub API status is {status} inside my Docker container!"

if __name__ == "__main__":
    print(get_greeting())