from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.api import app

from app.config import settings
from app.database import get_db
from app.database import Base
from alembic import command
import pytest
from app.oauth2 import create_access_token
from app import models


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Subbu@123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    # Drop and recreate tables to ensure a clean slate
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {"email": "gowtham@gmail.com", "password": "123456"}

    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {"email": "gowtham123@gmail.com", "password": "123456"}

    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })

    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [
        {
            "title": "first title",
            "content": "first content",
            "owner_id": test_user["id"]
        },
        {
            "title": "2nd title",
            "content": "2nd content",
            "owner_id": test_user["id"]
        },
        {
            "title": "3rd title",
            "content": "3rd content",
            "owner_id": test_user["id"]
        },
        {
            "title": "3rd title",
            "content": "3rd content",
            "owner_id": test_user2["id"]
        }

    ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    #     models.Post(title="first title", content="first content",
    #                 owner_id=test_user['id']),
    #     models.Post(title="2nd title", content="2nd content",
    #                 owner_id=test_user['id']),
    #     models.Post(title="3rd title", content="3rd content",
    #                 owner_id=test_user['id'])
    # ])
    session.commit()
    session.query(models.Post)

    posts = session.query(models.Post).all()
    return posts
