
from nose.tools import raises, eq_, ok_

from openmoo2.objects.system import StarSystem


class FakePlanet(object):
    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return "Planeta : {}".format(self.kind)


class TestSystem(object):
    planetA = FakePlanet("asteroids")
    planetB = FakePlanet("giant")
    planetC = FakePlanet("planet")
    planetD = None
    blackhole = StarSystem("hole", "black")

    def test_black_hole(self):
        eq_(self.blackhole.name, 'hole')
        eq_(self.blackhole.color, "black")

    def test_blackhole_planetes(self):
        eq_(self.blackhole.planets, {x+1: None for x in range(StarSystem.max_planets)})

    @raises(Exception)
    def test_add_planet_black_hole(self):
        self.blackhole.planets = self.planetD

    @raises(Exception)
    def test_add_administrator(self):
        self.blackhole.administrator = "Pepa z depa"

    def test_star(self):
        star = StarSystem("foo", "orange")
        eq_(star.color, "orange")
        eq_(star.name, "foo")
        eq_(star.administrator, None)
        eq_(star.planets, {})
        ok_('foo' in star._systems)

    def test_star_add_planet(self):
        star = StarSystem("boo", "orange")
        star.planets = "one"
        eq_(star.planets, {1: 'one'})

    @raises(Exception)
    def test_star_add_many_planets(self):
        star = StarSystem("baz", "orange")
        for i in range(StarSystem.max_planets+1):
            star.planets = self.planetC

    def test_rename_star(self):
        star = StarSystem("fii", "orange")
        eq_(star.name, 'fii')
        star.name = "faa"
        eq_(star.name, "faa")
        ok_("fii" not in star._systems)

    @raises(Exception)
    def test_rename_star_wrongly(self):
        x = StarSystem._systems[1]
        self.blackhole.name = x

    def test_star_administrator(self):
        star = StarSystem("Terra", "orange")
        eq_(star.administrator, None)
        star.administrator = "emperor"
        eq_(star.administrator, "emperor")
        del star.administrator
        eq_(star.administrator, None)
