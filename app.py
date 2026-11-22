import requests

def get_greeting():
    response = requests.get("https://api.github.com", timeout=5)
    if response.status_code == 200:
        return "Hello, World!"
    else:
        return "Failed to get greeting."

# This is now a real pytest test case:
def test_get_greeting():
    result = get_greeting()
    assert result == "Hello, World!"

if __name__ == "__main__":
    print(get_greeting())