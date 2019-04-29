import json
import pytest
import requests
from helpers.APIclient import APIClient 
from helpers.Endpoints import Endpoint

########### Tests for API https://dog.ceo/dog-api/ ################
########### set in console: "pytest -s tests/"     ################

#############################
headers = [ {}]  #{"Content-type": "text/html"} {"Content-type": "application/json"},
URL = "https://dog.ceo/api"

_endpoint = Endpoint()
endpoints = _endpoint.get_all_dict()
random_endpoints = _endpoint.get_random_endpoints()
multi_endpoints = _endpoint.get_multi_endpoints()
#############################


def pytest_addoption(parser):
    # add console params
    parser.addoption("--address", action="store", default=URL)


def params_list():
    # create urls + headers list
    params = [(method, header) for method in endpoints.values() for header in headers]
    return params


#@pytest.fixture(scope="module")
#def endpoints_list():
    #  endpoints list
 #   return endpoints


@pytest.fixture(scope="session", params=params_list())
def request_params(request):
    # url + header pairs 
    return (request.param[0], request.param[1])


@pytest.fixture(scope="session", params=random_endpoints)
def random_endpoint(request):
    # url for api/***/random endpoints 
    return (request.param)


@pytest.fixture(scope="session", params=multi_endpoints)
def multi_endpoint(request):
    # url for api/***/random/N endpoints 
    return (request.param)


@pytest.fixture(scope="session")
def client(request):
    return APIClient(request.config.getoption("--address"))


@pytest.fixture(scope="function")
def endpoint(request):
    return _endpoint


@pytest.fixture()
def breeds_response(request, client):
    # make GET ALL DOGS request
    response = client.do_get(endpoints["breeds"])
    resp_json = json.loads(response.content)
    return resp_json

