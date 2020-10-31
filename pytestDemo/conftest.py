import pytest


@pytest.fixture(scope='class')
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ['Bibhas', 'Biswas', 'rahulshettyacademy']


@pytest.fixture(params=[('Chrome','Bibhas','Biswas'), ('Firefox','Biswas'), ('IE', 'BB')])
def crossBrowser(request):
    return request.param

