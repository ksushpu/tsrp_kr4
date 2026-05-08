from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestUserCreation:

    def test_create_user_success(self):
        response = client.post("/task10_2/user", json={
            "username": "john",
            "age": 25,
            "email": "john@example.com",
            "password": "Secure123"
        })
        assert response.status_code == 201
        assert response.json()["username"] == "john"

    def test_age_validation(self):
        response = client.post("/task10_2/user", json={
            "username": "john",
            "age": 16,
            "email": "john@example.com",
            "password": "Secure123"
        })
        assert response.status_code == 422

    def test_email_validation(self):
        response = client.post("/task10_2/user", json={
            "username": "john",
            "age": 25,
            "email": "invalid-email",
            "password": "Secure123"
        })
        assert response.status_code == 422

    def test_password_length(self):
        response = client.post("/task10_2/user", json={
            "username": "john",
            "age": 25,
            "email": "john@example.com",
            "password": "123"
        })
        assert response.status_code == 422

    def test_default_phone(self):
        response = client.post("/task10_2/user", json={
            "username": "john",
            "age": 25,
            "email": "john@example.com",
            "password": "Secure123"
        })
        assert response.json()["phone"] == "Unknown"

    def test_age_19_valid(self):
        response = client.post("/task10_2/user", json={
            "username": "john",
            "age": 19,
            "email": "john@example.com",
            "password": "Secure123"
        })
        assert response.status_code == 201


class TestCustomExceptions:

    def test_exception_a_negative(self):
        response = client.get("/task10_1/check-condition?value=-5")
        assert response.status_code == 400
        assert "CUSTOM_A_ERROR" in response.json()["error_code"]

    def test_exception_a_zero(self):
        response = client.get("/task10_1/check-condition?value=0")
        assert response.status_code == 400

    def test_exception_b_not_found(self):
        response = client.get("/task10_1/product/999")
        assert response.status_code == 404
        assert "CUSTOM_B_ERROR" in response.json()["error_code"]

    def test_success_check(self):
        response = client.get("/task10_1/check-condition?value=42")
        assert response.status_code == 200

    def test_get_product_success(self):
        response = client.get("/task10_1/product/1")
        assert response.status_code == 200
        assert response.json()["name"] == "Ноутбук"