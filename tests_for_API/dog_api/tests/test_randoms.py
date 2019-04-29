import pytest
import requests
import json


@pytest.fixture(scope="function")
def random_response(request, client, random_endpoint):
    # make GET ALL DOGS request
    print("sent random request: ", random_endpoint)
    response = client.do_get(random_endpoint)
    resp_json = json.loads(response.content)
    return resp_json


@pytest.mark.usefixtures("random_response")
def test_value_in_message_is_str(random_response):
    assert isinstance(random_response["message"], str)


@pytest.mark.usefixtures("random_response")
def test_value_is_jpg_picture(random_response):
    assert ".jpg" in random_response["message"]


@pytest.mark.usefixtures("client", "random_endpoint")
def test_random_returns_diff_values(client, random_endpoint):
    # compare responses for method (Values must be different)

    first_image = json.loads(client.do_get(random_endpoint).content)["message"] 
    second_image = json.loads(client.do_get(random_endpoint).content)["message"] 
    third_image = json.loads(client.do_get(random_endpoint).content)["message"] 

    assert first_image != second_image or second_image != third_image or third_image != first_image

