import pytest


@pytest.mark.django_db
def test_ad_create(client, token, user, category):
    expected_response = {
        "id": 1,
        "is_published": False,
        "name": "test name ad",
        "price": 1000,
        "author": user.pk,
        "category": category.pk,
        "description": None,
        "image": None
    }

    data = {
        "category": category.pk,
        "name": "test name ad",
        "author": user.pk,
        "price": 1000
    }

    response = client.post(
        "/ads/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
