import pytest


@pytest.fixture
@pytest.mark.django_db
def token(client, django_user_model):
    username = "admin"
    password = "root789!"
    email = "admin"
    django_user_model.objects.create_user(
        username=username, password=password, role="admin", email=email
    )
    response = client.post(
        "/users/token/",
        {"username": username, "password": password},
        format="json"
    )
    return response.data["access"]
