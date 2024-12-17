import pytest
from fixture.application import Application


# инициализация фикстуры
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login('email', 'password')
    request.addfinalizer(fixture.destroy)
    return fixture