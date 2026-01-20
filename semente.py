from vascular_avascular import Vascular

class PlantaComSemente(Vascular):
    semente: bool = True

    def caracteristicas(self):
        return super().caracteristicas() + ["Possui sementes"]


class PlantaSemSemente(Vascular):
    semente: bool = False

    def caracteristicas(self):
        return super().caracteristicas() + ["Não possui sementes"]