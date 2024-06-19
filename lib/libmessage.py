from lib.liblog import *
log = liblog()

def default_invalid_field(field):
  m = f"field {field} is invalid, please try again."
  log.critical(m)
  return m