class Orcamento(object):

    def __init__(self, valor):
        # escondendo o valor
        self.__valor = valor

    # property para poder ler o valor
    @property
    def valor(self):
        return self.__valor
