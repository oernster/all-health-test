from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestClass:
    def test_hello_world(self):
        text = "Hello World"
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == "Hello World"

    def test_ingest(self):
        # sample data
        # num1 = 4
        # num2 = 99
        # response = client.post(
        #     "/ingest/",
        #     json={
        #         "num1": 4,
        #         "num2": 99,
        #     },
        # )
        # assert response.status_code == 200
        # assert response.json() == {
        #     "result": "103",
        # }
        pass
