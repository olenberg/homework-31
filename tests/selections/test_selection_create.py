import pytest


@pytest.mark.django_db
def test_create_selection(client, token, user, ad):
    expected_response = {
        "id": 1,
        "author": user.pk,
        "name": "Test name",
        "items": [ad.pk]
    }

    data = {
        "name": "Test name",
        "author": user.pk,
        "items": [ad.pk]
    }

    response = client.post(
        "/selections/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 201
    assert response.data == expected_response
