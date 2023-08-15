from basePage import BasePage
from interfaces import SetorI
from interfaces import TipoPedidoI
import time


class TipoPedido:
    def __init__(self, base_page: BasePage, data: TipoPedidoI, setor: SetorI):
        self.base_page = base_page
        self.data = data
        self.setor = setor

    def create(self):
        time.sleep(2)
        self.base_page.findAndClickArray(
            ["NavigationView_tree-FolderNotaFiscal", "NavigationView_tree-ItemClassificacaoTipodePedido"], isDuble=True)

        self.base_page.findAndClick("tb-Controle-Cadastrar")

        self.base_page.inputFormMultiple([
            {"id": "ClassificacaoTipoPedidoScreenDescriptor_codigoIntegracao",
                "value": self.data.codigo_integracao},
            {"id": "ClassificacaoTipoPedidoScreenDescriptor_descricao",
                "value": self.data.descricao},
        ])
        self.base_page.findAndClick(
            "ClassificacaoTipoPedidoScreenDescriptor_estadoMat")
        elements = self.base_page.finAllByCssSelector(
            "div.x-combo-list-item", all=True)
        time.sleep(5)

        for element in elements:
            if element.text == self.data.estado_material.item():
                element.click()
                break

        self.base_page.findAndClick(
            "ClassificacaoTipoPedidoScreenDescriptor_situacaoLote")
        elements = self.base_page.finAllByCssSelector(
            "div.x-combo-list-item", all=True)

        time.sleep(5)

        for element in elements:
            if element.text == self.data.situacao_lote.item():
                element.click()
                break

        time.sleep(20)

        self.base_page.findAndClick(
            "CadastroWindow_salvarCadastro-ClassificaçãoTipodePedidoButton")
        
        # self.base_page.awaitSave()
        # Click no primeiro resultado
        time.sleep(5)
        self.base_page.switchToCotext("slickGridFrame")
        self.base_page.findAndWrite(
            self.data.descricao, "filter-DESCRICAO", pressEnter=True)
        time.sleep(5)
        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()

        # Vincular Setoras a classificação
        self.base_page.findAndClick("tb-VincularaClassificacao-Setor")

        time.sleep(5)
        self.base_page.findAndWrite(
            "Descrição", "SiltTransfere_buscarComboBox")

        self.base_page.findAndWrite(
            self.data.setor, "SiltTransfere_buscarText", pressEnter=True)

        time.sleep(5)

        element = self.base_page.findByClass("x-grid3-col-MARCADO")
        element.click()
        self.base_page.findAndClick("SiltTransfere_fecharButton")
