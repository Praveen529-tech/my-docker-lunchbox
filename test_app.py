from app import check_github_status, get_greeting

def test_github_status():
    assert check_github_status() == 200

def test_get_greeting():
    assert "200" in get_greeting()