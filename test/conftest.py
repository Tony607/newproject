import pytest

IS_OLD = True
IS_YOUND = False

def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None

@pytest.fixture(scope="module", params=[("Ace",20, IS_YOUND), ("Bill", 45, IS_OLD)], ids=["young", "old"])
def person(request):
    from people import Person
    p = Person(request.param[0], request.param[1])
    return p

# @pytest.fixture(scope="session")
# def person():
#     from people import Person
#     p = Person("Tom Clark", 30)
#     yield p
#     print("teardown person")


