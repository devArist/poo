class Adresse:
    def __init__(self, rue:str, ville:str, code_postal:str):
        self.__rue = rue
        self.__ville = ville
        self.__code_postal = code_postal

    @property
    def rue(self):
        return self.__rue

    @property
    def ville(self):
        return self.__ville

    @property
    def code_postal(self):
        return self.__code_postal

    @rue.setter
    def nom(self, rue):
        self.__rue = rue

    @ville.setter
    def ville(self, ville):
        self.__ville = ville

    @code_postal.setter
    def code_postal(self, code_postal):
        self.__code_postal = code_postal