person_name = "Frank T"

class TestPeople(object):
    def test_is_old(self, person):
        old = person.is_old()
        assert old is False

    def test_get_nice_name(self, person):
        nice_name = person.get_nice_name()
        name = person.name
        assert name in nice_name

