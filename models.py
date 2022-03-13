from sqlalchemy import Column, Float, Integer
from db import Base

class Tarifa:

    def __init__(self, id):
        self.id_tarifa = id
        if id == 1:
            self.name = 'Naturgy'
        elif id == 2:
            self.name = 'Iberdrola'
        elif id == 3:
            self.name = 'Endesa'
        elif id == 4:
            self.name = 'Repsol'
        elif id == 5:
            self.name = 'EDP'
        else:
            print('ID no reconocido')

class Tarifa_estable(Tarifa):
    def __init__(self, id, precio_consumo):
        super().__init__(id)
        if self.id_tarifa == 1:
            self.kW = 3
        elif self.id_tarifa == 2:
            self.kW = 3.3
        elif self.id_tarifa == 3:
            self.kW = 3.9
        elif self.id_tarifa == 4:
            self.kW = 4.8
        elif self.id_tarifa == 5:
            self.kW = 3.48
        self.KWh = precio_consumo



class Cliente(Base):
    __tablename__ = "info_clientes"
    id = Column(Integer, primary_key=True)
    fac_1 = Column(Float)
    fac_2 = Column(Float)
    fac_3 = Column(Float)
    fac_4 = Column(Float)
    fac_5 = Column(Float)

    def __init__(self, naturgy, iber, endesa, repsol, edp):
        self.fac_1 = naturgy
        self.fac_2 = iber
        self.fac_3 = endesa
        self.fac_4 = repsol
        self.fac_5 = edp
