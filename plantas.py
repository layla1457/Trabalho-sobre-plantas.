class Plantas:
    def __init__(self, nomepopular: str, nomecientifico: str):
        self.__nomepopular = nomepopular
        self.__nomecientifico = nomecientifico

    def identificar(self):
        return f"{self.__nomepopular} ({self.__nomecientifico})"
