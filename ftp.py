from basePage import BasePage
from interfaces import Empresa
from interfaces import DataFtp

import time


class Ftp:
    def __init__(self, base_page: BasePage, data: Empresa, ftp_sheet: DataFtp):
        self.base_page = base_page
        self.data = data
        self.ftp = ftp_sheet

    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderConfiguracao",
                                          "NavigationView_tree-ItemConfiguracaodeIntegracao"], True)

        self.base_page.findAndClick("tb-ConfiguracaodeIntegracao-Cadastrar")
        self.base_page.findAndClick(
            "ConfiguracaoIntegracaoEntidadeScreenDescriptor_entidade-input")
        self.base_page.findAndWrite(
            self.data.razao_social, "SearchTriggerWindowRemote_searchTextField", pressEnter=True)

        time.sleep(2)
        elements = self.base_page.findByClass("x-grid3-col-CGC", all=True)

        for elemento in elements:
            if elemento.text == self.data.cnpj:
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")
        time.sleep(6)
       
        self.base_page.findAndClick(
            "ConfiguracaoIntegracaoEntidadeScreenDescriptor_armazem-input")
        
        time.sleep(2)
        elements = self.base_page.findByClass("x-grid3-col-DESCR", all=True)

        for elemento in elements:
            if elemento.text.upper() == self.data.armazem.upper():
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")
        self.base_page.findAndClick("CadastroWindow_menuTreePanel-Diretorios")
        time.sleep(2)
        self.base_page.inputFormMultiple([
            {"id": "ConfiguracaoIntegracaoDiretoriosScreenDescriptor_diretorioImportacao",
                "value": self.ftp.importacao},
            {"id": "ConfiguracaoIntegracaoDiretoriosScreenDescriptor_diretorioBackupImportacao",
                "value": self.ftp.backup_importacao},
            {"id": "ConfiguracaoIntegracaoDiretoriosScreenDescriptor_diretorioExportacao",
                "value": self.ftp.exportacao},
            {"id": "ConfiguracaoIntegracaoDiretoriosScreenDescriptor_diretorioBackupExportacao",
                "value": self.ftp.backup_exportacao},
            {"id": "ConfiguracaoIntegracaoDiretoriosScreenDescriptor_diretorioErro",
                "value": self.ftp.erro},
        ])

        self.base_page.findAndClick("CadastroWindow_salvarCadastroConfiguraçãodeIntegraçãoButton")
        time.sleep(2)
        self.base_page.findAndClick("WmsMessageBoxCONFIRM_YES_BUTTON")
        print("Create - FTP")
