import pytest


@pytest.mark.django_db
def test_ad_retrieve(client, ad, token):
    expected_response = {
        "id": ad.pk,
        "name": ad.name,
        "price": ad.price,
        "description": ad.description,
        "is_published": ad.is_published,
        "image": ad.image,
        "author": ad.author.pk,
        "category": ad.category.pk
    }

    response = client.get(
        f"/ads/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + token
    )

    assert response.status_code == 200
    assert response.data == expected_response
