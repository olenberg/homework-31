import pytest
from tests.factories import AdFactory
from ads.serializers import AdListSerializer


@pytest.mark.django_db
def test_ad_list(client):
    vacancies = AdFactory.create_batch(10)
    expected_response = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": AdListSerializer(vacancies, many=True).data
    }
    response = client.get("/ads/")
    assert response.status_code == 200
    assert response.data == expected_response
