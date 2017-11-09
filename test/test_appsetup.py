import pytest

class App(object):
    def __init__(self, p):
        self.person = p

@pytest.fixture(scope="module")
def app(person):
    return App(person)

def test_person_exists(app):
    assert app.person