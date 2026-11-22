from app import get_greeting

def test_get_greeting():
    assert get_greeting() == "Hello! I am running inside my own Docker container!"
