import pytest
import requests
import json

################ Tests for  api/breed/*/*/ endpoints ################

##################### SUB BREEDS IMAGES ########################
@pytest.fixture()
def sub_images_response(request, client, endpoint):
    # make GET sub breeds DOGS request
    response = client.do_get(endpoint.sub_images())
    resp_json = json.loads(response.content)
    return resp_json


@pytest.mark.usefixtures("sub_images_response")
def test_images_is_list(sub_images_response):
    assert isinstance(sub_images_response["message"], list)


@pytest.mark.parametrize("breed, sub, expected", [
    ("bulldog", "boston", True),
    ("ridgeback", "rhodesian", True),
    ("shihtzu", "bad_value", False),
    ("some_bad_value", "boston", False),
    ("12", "34", False)
], ids=["bulldog/boston", "ridgeback/rhodesian", "shihtzu/bad_value", "some_bad_value/boston", "12/34"])
@pytest.mark.usefixtures("client", "endpoint")
def test_get_images_by_sub_breed(breed, sub, expected, client, endpoint):
    # send api request with params

    url = endpoint.sub_images(breed = breed, sub_breed = sub)
    response = client.do_get(url) 
        
    assert response.ok == expected

    if expected:
        images = json.loads(response.content)["message"]
        assert isinstance(images, list)
        assert len(images) > 0


################################ SUB BREEDS ########################################
@pytest.fixture()
def sub_breeds_response(request, client, endpoint):
    # make GET sub breeds DOGS request
    response = client.do_get(endpoint.sub_breeds())
    resp_json = json.loads(response.content)
    return resp_json


@pytest.mark.usefixtures("sub_breeds_response")
def test_subs_is_list(sub_breeds_response):
    assert isinstance(sub_breeds_response["message"], list)


@pytest.mark.parametrize("breed, sub, in_list, expected", [
    ("bulldog", "boston", True, True),
    ("ridgeback", "shihtzu", False, True),
    ("shihtzu", "boston", False, True),
    ("some_bad_value", "boston", False, False),
    ("12", "34", False, False)
], ids=["bulldog/boston", "ridgeback/shihtzu", "shihtzu/boston", "some_bad_value/boston", "12/34"])
@pytest.mark.usefixtures("client", "endpoint")
def test_get_sub_by_breed(breed, sub, in_list, expected, client, endpoint):
    # send api request with params

    url = endpoint.sub_breeds(breed = breed)
    response = client.do_get(url) 
        
    assert response.ok == expected

    if expected:
        subs = json.loads(response.content)["message"]
        assert isinstance(subs, list)
        assert len(subs) >= 0
        assert (sub in subs) == in_list