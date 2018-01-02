from nota_fiscal import NotaFiscal
from datetime import datetime

class BuilderNotaFiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__itens = None
        self.__data_emissao = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_data_emissao(self, data_emissao):
        self.__data_emissao = data_emissao
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def build(self):
        if self.__razao_social is None:
            raise Exception('É necessário preencher a razão social.')
        if self.__cnpj is None:
            raise Exception('É necessário preencher o CNPJ.')
        if self.com_itens is None:
            raise Exception('É necessário que a nota tenha itens.')
        if self.__detalhes is None:
            self.__detalhes = ''
        if self.__data_emissao is None:
            self.__data_emissao = datetime.now()
        nf = NotaFiscal(razao_social=self.__razao_social, cnpj=self.__cnpj,
        itens=self.__itens, data_emissao=self.__data_emissao, detalhes=self.__detalhes)
        return nf