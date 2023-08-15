from basePage import BasePage
from interfaces import Empresa
import time
class Api:
    def __init__(self, base_page: BasePage, data: Empresa):
        self.base_page = base_page
        self.data = data

    def create(self):
        time.sleep(2)

        self.base_page.findAndClickArray(["NavigationView_tree-FolderConfiguracao",
                                          "NavigationView_tree-ItemConfiguracaodeIntegracao"], True)
        
        self.base_page.findAndClick("tb-ConfiguracaodeIntegracao-Cadastrar")
        self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_entidade-input")
        self.base_page.findAndWrite(self.data.razao_social,"SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        
        self.base_page.awaitSave("ext-el-mask-msg",class_name=True)
        time.sleep(2)

        elements = self.base_page.findByClass("x-grid3-col-CGC", all=True)

        for elemento in elements:
            if elemento.text == self.data.cnpj:
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")
        time.sleep(6)

        if self.data.integracao_via_servico_rest.upper() == 'SIM':
            self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_Integracão via Servico Rest")
            
        self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_armazem-input")
        time.sleep(2)
        elements = self.base_page.findByClass("x-grid3-col-DESCR", all=True)

        for elemento in elements:
            if elemento.text.upper() == self.data.armazem.upper():
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")
        time.sleep(5)
        self.base_page.findAndClick("CadastroWindow_salvarCadastroConfiguraçãodeIntegraçãoButton")
        print("Create - API REST")

        