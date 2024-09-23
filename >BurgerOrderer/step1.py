from flask import Flask
from flask import request
import os
import request

app = Flask(__name__)

Burgers= [{"name": "DemureChicken"},
          {"name": "HeroBurger"},
          {"name": "CutieHalloumi"}]

def getBurgers():
  return Burgers;


def presentFronypage():
  pg = "Welcome to BurgerOrderer"
  pg += "<P><UL>"

def visa_meny():
  menu = {
    ("1) DemureChiken")
    ("2) HeroBurger")
    ("3) CutieHalloumi")
  }

    
  
  
