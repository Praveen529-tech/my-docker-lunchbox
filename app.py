import requests

def get_greeting():
    return "Hello! I am running inside my own Docker container!"

if __name__ == "__main__":
    print(get_greeting())
