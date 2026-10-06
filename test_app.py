from app import app

def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert b"Hello" in r.data