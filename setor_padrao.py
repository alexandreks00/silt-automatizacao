from basePage import BasePage
from interfaces import SetorPadraoI
from interfaces import Empresa
import time


class SetorPadrao:
    def __init__(self, base_page: BasePage, sheet_setor_padrao: SetorPadraoI, empresa: Empresa):
        self.base_page = base_page
        self.data = sheet_setor_padrao
        self.empresa = empresa

    def create(self):
        self.base_page.findAndClickArray(
            ["NavigationView_tree-FolderCadastro", "NavigationView_tree-ItemDepositante"], isDuble=True)
        
        self.base_page.switchToCotext("slickGridFrame")
        
        self.base_page.findAndWrite(self.empresa.razao_social.item() ,"filter-RAZAOSOCIAL", pressEnter=True)
        time.sleep(5)
        
        self.base_page.findAndClick("rowNum-0")
        
        self.base_page.ReturnToMainContext()
        
        time.sleep(5)
        self.base_page.findAndClickByCss(
            "button.x-btn-text[style='position: relative; width: 12px;']")

        elements = self.base_page.finAllByCssSelector(
            "a.x-menu-item.x-component", all=True)

        for element in elements:
            if element.text == 'Setor Padrão':
                element.click()
                break
        
        time.sleep(5)
        self.base_page.findAndWrite(
            "Setor", "SiltTransfere_buscarComboBox")


        self.base_page.findAndWrite(self.data.prefix.item()+"%","SiltTransfere_buscarText",pressEnter=True)
        time.sleep(5)
        self.base_page.buttonDireito()
        self.base_page.findAndClick("SiltTransfere_GRID_MARCARTUDO")

        time.sleep(5)
        self.base_page.findAndWrite("%"+self.data.doca.item()+"%","SiltTransfere_buscarText",pressEnter=True)
        element = self.base_page.findAndClickByCss("div.x-grid3-col-MARCADO")

        time.sleep(5)
        self.base_page.findAndWrite("%"+self.data.bancada.item() +"%","SiltTransfere_buscarText",pressEnter=True)
        element = self.base_page.findAndClickByCss("div.x-grid3-col-MARCADO")

        time.sleep(2)
        self.base_page.findAndClick("SiltTransfere_fecharButton")
