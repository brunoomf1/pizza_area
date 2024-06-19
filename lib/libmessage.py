# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.
"""
Library to manage messages and log.
"""

from lib.liblog import *
log = liblog()

def default_invalid_field(field):
  """
  Default message for invalid field.

  Args:
      field (str): The name of the invalid field.

  Returns:
      str: The default message.
  """
  m = f"field {field} is invalid, please try again."
  log.critical(m)
  return m
