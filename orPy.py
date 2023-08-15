from basePage import BasePage
from interfaces import Empresa
from interfaces import SetorI
from interfaces import DataOr
import time


class Or:
    def __init__(self, base_page: BasePage, data: SetorI, data_or: DataOr, data_empresa: Empresa):
        self.base_page = base_page
        self.data = data
        self.data_or = data_or
        self.data_empresa = data_empresa

    def create(self):
        time.sleep(2)
        self.base_page.findAndClickArray(
            ["NavigationView_tree-FolderCadastro", "NavigationView_tree-ItemDepositante"], True)
        
        self.base_page.switchToCotext("slickGridFrame")
        self.base_page.findAndWrite(
            self.data_empresa.razao_social, "filter-RAZAOSOCIAL", pressEnter=True)
        time.sleep(2)
        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()
        self.base_page.findAndClickByCss(
            "button.x-btn-text[style='position: relative; width: 12px;']")

        elements = self.base_page.finAllByCssSelector(
            "a.x-menu-item.x-component", all=True)

        for element in elements:
            if element.text == 'Conf. OR Automática':
                element.click()
                break

        self.base_page.findAndClick("DepositanteConfiguracaoORAutomaticaScreenDescriptor_tipoRecebimento-input")
        
        self.base_page.findAndWrite(self.data_or.codigo_tipo_recebimento,
                                    "SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        

        time.sleep(15)
        elements =  self.base_page.finAllByCssSelector("div.x-grid3-cell-inner.x-grid3-col-TIPORECEBIMENTO", all=True)
        for element in elements:
            if element.text == self.data_or.codigo_tipo_recebimento.item():
                element.click()
                break
        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        self.base_page.findAndClick("DepositanteConfiguracaoORAutomaticaScreenDescriptor_doca-input")

        self.base_page.findAndWrite(self.data_or.codigo_doca.item(),
                                    "SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        

        time.sleep(15)
        elements =  self.base_page.finAllByCssSelector("div.x-grid3-col-Doca", all=True)
        for element in elements:
            if element.text ==  '0'+str(self.data_or.codigo_doca.item()):
                element.click()
                break
            print(element.text)
            print( self.data_or.codigo_doca.item())
        
        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        
        self.base_page.inputFormMultiple([
            {"id":"DepositanteConfiguracaoORAutomaticaScreenDescriptor_placaVeiculo", "value":self.data_or.placa_veiculo.item()},
            {"id":"DepositanteConfiguracaoORAutomaticaScreenDescriptor_qtdVolume", "value":self.data_or.quantidade_volume_recebido.item()},
            {"id":"DepositanteConfiguracaoORAutomaticaScreenDescriptor_intervaloIntegracao", "value":self.data_or.intervalo_integracao.item()},

        ])

        self.base_page.findAndClickByCss("button.x-btn-text[style='position: relative; width: 69px;']")
