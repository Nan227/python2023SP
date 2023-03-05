F_FREEZING = 32.0
F_SCALE = 9/5

# def degF(degC):
#   scaled = degC*9/5
#   result = scaled + F_FREEZING
#   return result

def degF(degC):
  return F_SCALE*degC + F_FREEZING
