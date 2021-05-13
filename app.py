from src.lightsaber import Lightsaber
from src.lasergun import LaserGun
from src.telepod import Telepod
from src.movie import Movie

prop_1 = Lightsaber()
prop_2 = LaserGun()
prop_3 = Telepod()
movie_1 = Movie("Star Wars")
movie_2 = Movie("The Fly")

print(movie_1.use_prop(prop_1))
print(movie_1.use_prop(prop_2))
print(movie_2.use_prop(prop_3))


