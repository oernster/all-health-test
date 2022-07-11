import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestClass:
    def setup(self):
        self.input_data = {
            "timestamp": 41456,
            "base": 'EUR',
            "date": '2011-05-07',
            "rates": 'GBP: 123, USD: 456',
        }

    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_ingest(self):
        self.setup()
        response = client.post(
            "/ingest",
            json=self.input_data,
        )
        assert response.status_code == 200
        assert response.json()['timestamp'] == self.input_data['timestamp']
        assert response.json()['base'] == self.input_data['base']
        assert response.json()['date'] == self.input_data['date']
        assert response.json()['rates'] == self.input_data['rates']
        assert 'updated' in response.json().keys()

    def test_exchange_rates(self):
        self.setup()
        response = client.get(
            "/exchange_rates/EUR",
        )
        assert response.status_code == 200
        assert response.json()['timestamp'] == self.input_data['timestamp']
        assert response.json()['base'] == self.input_data['base']
        assert response.json()['date'] == self.input_data['date']
        assert response.json()['rates'] == self.input_data['rates']
        assert 'updated' in response.json().keys()
