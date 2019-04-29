import pytest
import requests
import json


@pytest.fixture(scope="function")
def get_response(request, client, request_params):
    # make GET request and return response
    print(f'''sent request for test "{request.keywords.node.name}" with params: {request_params[0]}, {request_params[1]} ''')
    response = client.do_get(endpoint = request_params[0], headers = request_params[1])
    return response


@pytest.mark.usefixtures("get_response")
def test_status_code_is_200(get_response):
    assert get_response.status_code == 200


@pytest.mark.usefixtures("get_response")
def test_success_response(get_response):
    assert get_response.ok


@pytest.mark.usefixtures("get_response")
def test_content_is_json_with_text(get_response):
    # test repsonse - it must be json format with text values, and with some data
    assert isinstance(get_response.text, str)
    assert get_response.headers['Content-type'] == "application/json"
    assert '{' in get_response.text


@pytest.fixture()
def content_response(request, get_response):
    # make GET ALL DOGS request
    resp_json = json.loads(get_response.content)
    return resp_json


@pytest.mark.usefixtures("content_response")
def test_field_status_success(content_response):
    assert content_response["status"] == 'success'
    
