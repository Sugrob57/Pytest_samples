import pytest
import requests
import json

############### Tests for  api/****/random endpoints ################

@pytest.fixture()
def breed_response(request, client, endpoint):
    # make GET breed DOGS request
    response = client.do_get(endpoint.breed_images())
    resp_json = json.loads(response.content)
    return resp_json


@pytest.mark.usefixtures("breed_response")
def test_field_message_is_list(breed_response):
    assert isinstance(breed_response["message"], list)


@pytest.mark.parametrize("test_input, expected", [
    ("bulldog", True),
    ("ridgeback", True),
    ("shihtzu", True),
    ("some_bad_value",False),
    ("12",False)
], ids=["bulldog", "ridgeback", "shihtzu", "some_bad_value", "12"])
@pytest.mark.usefixtures("client", "endpoint")
def test_requests_by_breed(test_input, expected, client, endpoint):
    # send api request with params

    url = endpoint.breed_images(test_input)
    response = client.do_get(url) 

    assert response.ok == expected

    if expected:
        images = json.loads(response.content)["message"]
        assert isinstance(images, list)
        assert (len(images) > 0) == expected

