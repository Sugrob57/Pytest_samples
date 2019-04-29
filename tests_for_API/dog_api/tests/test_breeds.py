import pytest
import requests
import json


@pytest.mark.usefixtures("breeds_response")
def test_field_message_is_list(breeds_response):
    assert isinstance(breeds_response["message"], dict)


@pytest.mark.usefixtures("breeds_response", "client", "endpoint")
def test_compare_allBreads_with_subBreads(breeds_response, client, endpoint):
    # compare data from ALL BREED message item
    # and SUB BREED item

    # find first record with data
    for _first_breed, _sub_breads in breeds_response["message"].items():
        if len(_sub_breads) > 0:
            break
    
    # make request GET SUB_BREEDS
    url = endpoint.sub_breeds(_first_breed)
    sub_response = client.do_get(url)
    sub_breeds = json.loads(sub_response.content)

    # create lists for comparation
    original_list = _sub_breads # it's data from get all breeds response
    sub_list = sub_breeds["message"] # it's data from get sub breeds response

    assert len(original_list) == len(sub_list)
    assert original_list[0] == sub_list[0]

