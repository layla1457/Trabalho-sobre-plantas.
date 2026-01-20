from vascular_avascular import Avascular
from semente import PlantaSemSemente
from fruto import SemFruto, ComFruto

class Briofita(Avascular):
    plantas: list = []

    @classmethod
    def listar(cls):
        return cls.plantas


class Pteridofita(PlantaSemSemente):
    plantas: list = []

    @classmethod
    def listar(cls):
        return cls.plantas


class Gimnosperma(SemFruto):
    plantas: list = []

    @classmethod
    def listar(cls):
        return cls.plantas


class Angiosperma(ComFruto):
    plantas: list = []

    @classmethod
    def listar(cls):
        return cls.plantas