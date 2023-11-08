import requests
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
@pytest.fixture()
def sample_fixture():
    print("this is a fixture before test case")

    yield
    print("Fixture after test case")
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.smoke
def test_getrequest(sample_fixture):
    url="http://localhost:9000/api/maincategory/"

    response=requests.get(url)
    assert response.status_code==200
@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.sanity
def test_getrequest2(sample_fixture):
    url="http://localhost:9000/api/subcategory/"

    response=requests.get(url)
    assert response.status_code==200