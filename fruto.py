from semente import PlantaComSemente

class ComFruto(PlantaComSemente):
    fruto: bool = True

    def caracteristicas(self):
        return super().caracteristicas() + ["Possui fruto"]


class SemFruto(PlantaComSemente):
    fruto: bool = False

    def caracteristicas(self):
        return super().caracteristicas() + ["Não possui fruto"]
