from basePage import BasePage
from interfaces import TransportadoraI
from interfaces import Empresa
import time


class Transportadora:
    def __init__(self, base_page: BasePage, data: TransportadoraI, empresa: Empresa):
        self.base_page = base_page
        self.data = data
        self.empresa = empresa

    def create_servico(self, servico):

        print(servico)
        print(servico)
        print(servico)
        
        self.base_page.findAndWrite(
            servico.cnpj_transportadora, "SiltTransfere_buscarText")
        time.sleep(1)
        self.base_page.findAndClick("SiltTransfere_buscarButton")
        time.sleep(2)

        elemento = self.base_page.find_element_by_css("td.x-grid3-td-MARCADO > div.x-grid3-cell-inner > span > img")

        src_value = elemento.get_attribute("src")

        print("Valor do atributo 'src':", src_value)

        # Verifica se a imagem é a imagem desmarcada (unchecked)
        if "images/icons/check-box-icon-unchecked.png" in src_value:

            self.base_page.findAndClickByCss("td > div > span > img")
            print("Elemento marcado com sucesso.")
        else:
            print("O elemento já está com check e será ignorado.")

        self.base_page.findAndClickByCss("div.x-grid3-body")

        time.sleep(2)
        self.base_page.findAndClick("tb-ServicosdaTransportadora")
        self.base_page.driver.maximize_window()
        self.base_page.findAndClick("tb-Cadastro-Cadastrar")

        self.base_page.findAndWrite(
            servico.codigo_servico_exportacao, "ConfServicoTransportadoraScreenDescriptor_codigoservicoexportacao")

        self.base_page.findAndWrite(
            servico.codigo_servico, "ConfServicoTransportadoraScreenDescriptor_codigoservico")
        
        self.base_page.findAndWrite(
            servico.descricao, "ConfServicoTransportadoraScreenDescriptor_descricao")
        
        self.base_page.findAndClick("ConfServicoTransportadoraScreenDescriptor_modeloEtiquetaServicoTransportadora-input")
        time.sleep(1)

        self.base_page.findAndWrite(
            servico.modelo_etiqueta, "SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        time.sleep(2)

        self.base_page.findAndClickByCss("div.x-grid3-col-DESCR")

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        self.base_page.findAndClick("CadastroWindow_salvarCadastroServiçodaTransportadoraButton")

        self.base_page.findAndClick("GridWindow_fecharButton")
        self.base_page.driver.minimize_window()


    def create_transportadora(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                         "NavigationView_tree-ItemDepositante"], True)

        self.base_page.switchToCotext("slickGridFrame")

        self.base_page.findAndWrite(
            self.empresa.razao_social, "filter-RAZAOSOCIAL", pressEnter=True)
        time.sleep(3)
       
        self.base_page.findAndClick("rowNum-0")

        self.base_page.ReturnToMainContext()

        self.base_page.driver.minimize_window()

        self.base_page.findAndClickByCss(
            "button.x-btn-text[style='position: relative; width: 12px;']")
        elements = self.base_page.finAllByCssSelector(
            "a.x-menu-item.x-component", all=True)

        for element in elements:
            if element.text == 'Transp. e Rastreamento':
                element.click()
                break

        self.base_page.findAndClick("SiltTransfere_buscarComboBoxComboArrow")
        self.base_page.findAndClick("SiltTransfere_buscarComboBox-CNPJTRANSPORTADORA")

        #10
        for servico in self.data.itertuples(index=False):
            self.create_servico(servico)
        