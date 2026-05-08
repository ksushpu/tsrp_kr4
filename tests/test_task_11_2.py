import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app
from faker import Faker

fake = Faker('ru_RU')

@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

@pytest.fixture
def generate_user():
    return {
        "username": fake.user_name(),
        "age": fake.random_int(min=19, max=100),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number()
    }

@pytest.mark.asyncio
async def test_create_user_async(async_client, generate_user):
    response = await async_client.post("/task10_2/user", json=generate_user)
    assert response.status_code == 201
    assert response.json()["username"] == generate_user["username"]

@pytest.mark.asyncio
async def test_invalid_age_async(async_client, generate_user):
    generate_user["age"] = 16
    response = await async_client.post("/task10_2/user", json=generate_user)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_invalid_email_async(async_client, generate_user):
    generate_user["email"] = "invalid"
    response = await async_client.post("/task10_2/user", json=generate_user)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_short_password_async(async_client, generate_user):
    generate_user["password"] = "123"
    response = await async_client.post("/task10_2/user", json=generate_user)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_exception_a_async(async_client):
    response = await async_client.get("/task10_1/check-condition?value=-1")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_exception_b_async(async_client):
    response = await async_client.get("/task10_1/product/999")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_health_async(async_client):
    response = await async_client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"