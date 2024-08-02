from lib.libarea import *
from lib.libdb import *
from lib.libquerydb import *
from lib.libutils import *
from lib.libmodels import *
from lib.liblog import *


def eng_pizza_calculate(diameter = float, n_people = int):
    p_area = pizza_area()
    p_area.configure(diameter, n_people)
    p_area.process()
    response = p_area.get_pizza_info()
    return response