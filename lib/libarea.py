import math as mt
from lib.libmessage import *

DEFAULT_N_SLICE = 12

class pizza_area():
  def __init__(self):
    self.d = 0
    self.r = 0
    self.area = 0
    self.n_people = 0
    self.n_area = 0
    self.s_area = 0

  def set_n_people(self,n_people):
    if n_people <= 0:
      return default_invalid_field(f'{n_people} empty')
    self.n_people = n_people

  def calc_d_to_r(self,diameter):
    if diameter <= 0:
      return default_invalid_field(f'diameter, is {diameter}')
    r = diameter/2
    r = round(r,2)
    self.r = r
    self.d = diameter

  def total_area(self):
    pi = round(mt.pi,4)
    r = self.r
    area = pi*r**2
    self.area = area
    self.s_area = area/DEFAULT_N_SLICE

  def calc_area_for_n_people(self):
    n_people = self.n_people
    if not n_people:
      return default_invalid_field(f'n_people is {n_people}')
    if n_people <= 0:
      return default_invalid_field(f'n_people is {n_people}')
    area = (self.area)
    n_area = area/n_people
    self.n_area = n_area
  
  def n_slice_for_people(self):
    n_slice = self.n_area/self.s_area
    return n_slice

  def configure(self,diameter,n_people):
    self.calc_d_to_r(diameter)
    self.set_n_people(n_people)
    self.total_area()
  
  def process(self):
    self.calc_area_for_n_people()
  
  def get_pizza_info(self):
    n_slice = self.n_slice_for_people()
    return self.n_people, self.n_area, self.d, n_slice