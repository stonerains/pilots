from selfdrive.car import STD_CARGO_KG
from selfdrive.car.hyundai.values_community import CAR

def get_params(candidate, ret):
  tire_stiffness_factor = 0.8

  if candidate in [CAR.GRANDEUR_IG, CAR.GRANDEUR_IG_HEV]:
    ret.mass = 1570. + STD_CARGO_KG
    ret.wheelbase = 2.845
    ret.steerRatio = 16.
    tire_stiffness_factor = 0.8
    ret.centerToFront = ret.wheelbase * 0.385
  elif candidate in [CAR.GRANDEUR_IG_FL, CAR.GRANDEUR_IG_FL_HEV]:
    ret.mass = 1600. + STD_CARGO_KG
    ret.wheelbase = 2.885
    ret.steerRatio = 17.
    tire_stiffness_factor = 0.8
    ret.centerToFront = ret.wheelbase * 0.385
  elif candidate == CAR.GENESIS_EQ900:
    ret.mass = 2200
    ret.wheelbase = 3.15
    ret.steerRatio = 16.0
    ret.steerActuatorDelay = 0.075
  elif candidate == CAR.GENESIS_EQ900_L:
    ret.mass = 2290
    ret.wheelbase = 3.45
  elif candidate == CAR.GENESIS_G90:
    ret.mass = 2150
    ret.wheelbase = 3.16
  elif candidate == CAR.MOHAVE:
    ret.mass = 2285. + STD_CARGO_KG
    ret.wheelbase = 2.895
  elif candidate in [CAR.K7, CAR.K7_HEV]:
    ret.mass = 1850. + STD_CARGO_KG
    ret.wheelbase = 2.855
    ret.steerRatio = 15.5
    tire_stiffness_factor = 0.7
  elif candidate == CAR.K9:
    ret.mass = 2075. + STD_CARGO_KG
    ret.wheelbase = 3.15
    ret.steerRatio = 14.5
    tire_stiffness_factor = 0.8

  return tire_stiffness_factor
