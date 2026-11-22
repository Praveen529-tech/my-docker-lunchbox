import requests

def get_greeting():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        return "Hello, World!"
    else:
        return "Failed to get greeting."

get_greeting()

if __name__ == "__main__":
    print(get_greeting())