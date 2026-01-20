from plantas import Plantas

class Vascular(Plantas):
    vasos: bool = True

    def caracteristicas(self):
        return ["Possui vasos condutores"]


class Avascular(Plantas):
    vasos: bool = False

    def caracteristicas(self):
        return ["Não possui vasos condutores, nem sementes e nem frutos."]