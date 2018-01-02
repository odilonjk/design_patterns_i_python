from datetime import datetime
from item import Item

class NotaFiscal(object):
    def __init__(self, razao_social, cnpj, itens, data_emissao=datetime.now(), detalhes=''):
        self.__razao_sozial = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_emissao = data_emissao
        self.__detalhes = detalhes
    
    @property
    def razao_social(self):
        return self.__razao_sozial

    @razao_social.setter
    def razao_social(self, razao_social):
        self.__razao_sozial = razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, itens):
        self.__itens = itens

    @property
    def detalhes(self):
        return self.__detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        self.__detalhes = detalhes

    @property
    def data_emissao(self):
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao):
        self.__data_emissao = data_emissao

    def __str__(self):
        return 'Razão Social: {:s}\nData de emissão: {:%d-%m-%Y %H:%M:%S}\n'.format(self.razao_social, self.data_emissao)

if __name__ == '__main__':
    
    from builder_nota_fiscal import BuilderNotaFiscal

    item = Item(codigo='WWIIP.1', descricao='Republic P-47', valor=1758528.00)

    nf = (BuilderNotaFiscal()
          .com_cnpj('0123456789')
          .com_razao_social('USAF')
          .com_itens({item}).build())

    print(nf)
    print('Itens--------\n')
    for i in nf.itens:
        print(i)