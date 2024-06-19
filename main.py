# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.

from lib.libarea import *

diameter = 35
n_people = 2
pizza_area = pizza_area()
pizza_area.configure(diameter,n_people)
pizza_area.process()

n_people,area,diameter,n_slice = pizza_area.get_pizza_info()

m = f"In a {diameter} cm pizza, {n_people} will consume approximately {area}cm^2, which is equivalent to {n_slice} slices of a 12-slice pizza."
print(m)