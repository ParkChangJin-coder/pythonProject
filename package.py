# animal package
# dog, cat modules
# dog, cat modules can say "hi"

from animal import dog
from animal import cat

from animal import * # animal 패키지가 갖고있는 모듈을 다 불러라
d2 = Dog()
c2 = Cat()
d2.hi()
c2.hi()

d = dog.Dog()
d.hi()

c = cat.Cat()
c.hi()