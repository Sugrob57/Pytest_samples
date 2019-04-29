import pytest
import requests
import json

######## Tests for  api/****/random/COUNT endpoints ################

@pytest.fixture(scope="function")
def multi_response(request, client, multi_endpoint):
    # make GET random list
    print("sent multi request: ", multi_endpoint)
    response = client.do_get(multi_endpoint)
    resp_json = json.loads(response.content)
    return resp_json


@pytest.mark.usefixtures("multi_response")
def test_value_in_message_is_dict(multi_response):
    # value for multi request must be LIST
    assert isinstance(multi_response["message"], list)


@pytest.mark.usefixtures("multi_response")
def test_value_is_jpg_picture(multi_response):
    # every record in response must have *.JPG extension
    assert ".jpg" in multi_response["message"][0]


@pytest.mark.usefixtures("client", "multi_endpoint")
def test_random_returns_diff_values(client, multi_endpoint):
    # compare responses for method (Values must be different)

    first = json.loads(client.do_get(multi_endpoint).content)["message"] 
    second = json.loads(client.do_get(multi_endpoint).content)["message"] 
    third = json.loads(client.do_get(multi_endpoint).content)["message"] 

    assert first != second or second != third or third != first


@pytest.mark.parametrize("test_input,expected", [
    (5, True),
    ("TWO", False),
    (1000, True)
], ids=["get 5", "get TWO", "get 1000"])
@pytest.mark.usefixtures("client", "endpoint")
def test_param_count_records(test_input, expected, client, multi_endpoint):
    # request N records from api/***/random/N endpoints
    url = multi_endpoint.replace("3", str(test_input))
    response = client.do_get(url)

    assert response.ok == expected 
    if expected:
        msg = json.loads(response.content)["message"]
        assert isinstance(msg, list) == expected 
        assert 0 < len(msg) <= test_input
        

