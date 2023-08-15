from basePage import BasePage
from interfaces import SetorI
from interfaces import Empresa

import time


class Setor:
    def __init__(self, base_page: BasePage, data: SetorI, empresa: Empresa):
        self.base_page = base_page
        self.data = data
        self.empresa = empresa

    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                         "NavigationView_tree-FolderCadastroArmazem", "NavigationView_tree-ItemSetor"], True)

        self.base_page.findAndClick("tb-Controle-Cadastrar")

        self.base_page.findAndWrite(
            self.data.setor_armazenagem, "SetorScreenDescriptor_descricao")

        self.base_page.findAndWrite(
            self.data.codigo_integracao, "SetorScreenDescriptor_codigoIntegracao")

        self.base_page.findAndClick("SetorScreenDescriptor_area-input")

        self.base_page.findAndWrite(
            self.data.area_setor, "SearchTriggerWindowRemote_searchTextField")

        self.base_page.pressEnter("SearchTriggerWindowRemote_searchTextField")

        time.sleep(2)
        areas_setores = self.base_page.findByClass(
            "x-grid3-col-AREA", all=True)

        for elemento in areas_setores:
            if elemento.text == self.data.area_setor:
                time.sleep(5)
                elemento.click()
                break
        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        time.sleep(2)

        self.base_page.findAndClick("SetorScreenDescriptor_tipoSetor-input")
        self.base_page.findAndWrite(
            self.data.tipo_setor, "SearchTriggerWindowRemote_searchTextField")
        self.base_page.pressEnter("SearchTriggerWindowRemote_searchTextField")

        time.sleep(2)

        tipos_setores = self.base_page.findByClass(
            "x-grid3-col-TIPOSETOR", all=True)

        for elemento in tipos_setores:
            if elemento.text == self.data.tipo_setor:
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        if self.data.permite_expedicao_produto.upper() == 'SIM':
            self.base_page.findAndClick(
                "SetorScreenDescriptor_Permite Expedicão de Produto")
        if self.data.permite_mais_produto_pulmao.upper() == 'SIM':
            self.base_page.findAndClick(
                "SetorScreenDescriptor_Permite mais de um produto no pulmão")

        self.base_page.findAndClick(
            "CadastroWindow_salvarCadastrodeSetorButton")

        print("Create - Setor - "+ str(self.data.setor_armazenagem))

    def createDepositante(self):
        time.sleep(5)
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                            "NavigationView_tree-FolderCadastroArmazem", "NavigationView_tree-ItemSetor"], True)

        self.base_page.switchToCotext("slickGridFrame")

        self.base_page.findAndWrite(
            self.data.setor_armazenagem, "filter-SETOR", pressEnter=True)
        time.sleep(10)
       
        self.base_page.findAndClick("rowNum-0")

        self.base_page.ReturnToMainContext()
        self.base_page.findAndClick("tb-VincularaoSetor-Depositantes")
        time.sleep(2)
        self.base_page.findAndClick("SiltTransfere_buscarComboBoxComboArrow")
        time.sleep(2)
        self.base_page.findAndClick("SiltTransfere_buscarComboBox-RAZAOSOCIAL")

        self.base_page.findAndWrite(
            self.empresa.razao_social, "SiltTransfere_buscarText", pressEnter=True)
        time.sleep(2)
        self.base_page.findAndClickByClass("x-grid-cell-first")
        time.sleep(3)
        self.base_page.findAndClick("tb-DefinirCodigodeIntegracao")
        time.sleep(3)
        self.base_page.insert_value_integration(self.data.codigo_integracao)
        time.sleep(3)
        self.base_page.button_value_integration()
        time.sleep(3)
        self.base_page.findAndClick("SiltTransfere_fecharButton")
        print("Create - Depositante - "+str(self.data.setor_armazenagem))
        self.base_page.reaload()

    def tipo_recebimento(self, tipos):
        time.sleep(5)
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroArmazem", "NavigationView_tree-ItemSetor"], True)
       
        time.sleep(5)
        self.base_page.switchToCotext("slickGridFrame")
        time.sleep(2)

        self.base_page.findAndWrite(
            self.data.setor_armazenagem, "filter-SETOR", pressEnter=True)
        time.sleep(10)

        self.base_page.findAndClick("rowNum-0")

        self.base_page.ReturnToMainContext()
        self.base_page.findAndClick("tb-VincularaoSetor-TiposdeRecebimento")
        time.sleep(5)
        self.base_page.findAndClick("SiltTransfere_buscarComboBoxComboArrow")
        time.sleep(5)
        self.base_page.findAndClick(
            "SiltTransfere_buscarComboBox-TIPORECEBIMENTO")
        time.sleep(2)
        element = self.base_page.findById("SiltTransfere_buscarText")
        if len(tipos) > 0:
            for tipo in tipos:
                self.base_page.findAndWrite(
                    tipo, "SiltTransfere_buscarText", pressEnter=True)
                time.sleep(5)

                self.base_page.findAndClick("grid_row_0")
                element.clear()

        self.base_page.findAndClick("SiltTransfere_fecharButton")

        print("Create - Tipo Recebimento - "+ str(self.data.setor_armazenagem))

    def regiao_armazenagem(self, data):
        time.sleep(10)
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroArmazem", "NavigationView_tree-ItemRegiaodeArmazenagem"], True)     
        self.base_page.findAndClick("tb-Controle-Cadastrar")
        self.base_page.findAndWrite(
            data.regiao_armazenagem, "RegiaoDeArmazenagemScreenDescriptor_descricao")
        self.base_page.findAndClick("RegiaoDeArmazenagemScreenDescriptor_tipo")

        elements = self.base_page.findByClass("x-combo-list-item ", all=True)

        for elemento in elements:
            if elemento.text == data.tipo_armazenagem:
                elemento.click()
                break
        
        self.base_page.findAndClick("CadastroWindow_salvarCadastrodeRegiãodeArmazenagemButton")
        print("Create - Regiao Armazenagem - " + str( data.regiao_armazenagem))
