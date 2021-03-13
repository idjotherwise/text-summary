def test_ping(test_app):
    # Given: (setup code, fixtures, database state)
    # test_app (which is the fixture defined in conftest.py, and is passed in as an argument to this function
    # When: (code under test)
    response = test_app.get("/ping")

    # Then: (asserts)
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": True}
