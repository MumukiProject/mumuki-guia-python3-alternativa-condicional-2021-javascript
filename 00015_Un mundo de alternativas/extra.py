def listo(): 
  pass

def saludar_a(quien, horario):
  if horario < 12:
    return "Buenos días " + quien
  elif horario < 19:
    return "Buenas tardes " + quien
  else: 
    return "Buenas noches " + quien
    
def saludar_a_recargado(quien, horario):
  if horario < 19:
    return "Buenas tardes " + quien
  elif horario < 12:
    return "Buenos días " + quien
  else: 
    return "Buenas noches " + quien
    