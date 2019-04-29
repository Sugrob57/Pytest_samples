import json
import pytest


endpoints = dict()


@pytest.mark.parametrize("endpoint", endpoints)
def test_endpoints_encoding(client, endpoint):
    response = client.do_get(endpoint)
    assert response.status_code == 200
    assert isinstance(response.text, str)


@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
], ids=["3+5", "2+4", "6*9"])
def test_eval(test_input, expected):
    assert eval(test_input) == expected



##########################
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    print("a_fixture")
    return request.param


def test_a(a):
    print("a:", a)


def idfn(fixture_value):
    print("idfn", fixture_value)
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    print("b_fixture")
    return request.param


def test_b(b):
    print("b:", b)